import { LightningElement, track, wire } from 'lwc';
import { NavigationMixin } from 'lightning/navigation';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import getAllPapersWithMetrics from '@salesforce/apex/EreunaController.getAllPapersWithMetrics';
import { refreshApex } from '@salesforce/apex';

export default class PaperExplorer extends NavigationMixin(LightningElement) {
    @track searchKey = '';
    @track selectedDiscipline = 'All';
    @track isCardView = true;
    @track expandedMap = {};
    @track isLoading = true;

    wiredPapersResult;
    rawPapers = [];

    @wire(getAllPapersWithMetrics, { discipline: '$selectedDiscipline', searchKey: '$searchKey' })
    wiredPapers(result) {
        this.wiredPapersResult = result;
        const { data, error } = result;
        if (data) {
            this.rawPapers = data;
            this.isLoading = false;
        } else if (error) {
            this.isLoading = false;
            this.showToast('Error Loading Papers', error.body?.message || 'Failed to fetch literature catalog.', 'error');
        }
    }

    get filteredPapers() {
        if (!this.rawPapers) {
            return [];
        }
        return this.rawPapers.map(paper => {
            const isExpanded = !!this.expandedMap[paper.Id];
            const metrics = paper.Extracted_Metrics__r || [];
            const doiUrl = paper.DOI__c ? (paper.DOI__c.startsWith('http') ? paper.DOI__c : `https://doi.org/${paper.DOI__c}`) : null;

            return {
                ...paper,
                doiUrl,
                hasMetrics: metrics.length > 0,
                metricsList: metrics,
                abstractClass: isExpanded ? 'abstract-text expanded' : 'abstract-text clamped',
                expandLabel: isExpanded ? 'Show Less' : 'Read Abstract',
                isExpanded
            };
        });
    }

    get hasPapers() {
        return this.filteredPapers && this.filteredPapers.length > 0;
    }

    get totalCountLabel() {
        return `${this.filteredPapers.length} Publications Cataloged`;
    }

    get allVariant() {
        return this.selectedDiscipline === 'All' ? 'brand' : 'neutral';
    }

    get cloudVariant() {
        return this.selectedDiscipline === 'Cloud Computing' ? 'brand' : 'neutral';
    }

    get distVariant() {
        return this.selectedDiscipline === 'Distributed Systems' ? 'brand' : 'neutral';
    }

    get cardViewVariant() {
        return this.isCardView ? 'brand' : 'border';
    }

    get tableViewVariant() {
        return !this.isCardView ? 'brand' : 'border';
    }

    handleSearchChange(event) {
        window.clearTimeout(this.delayTimeout);
        const val = event.target.value;
        this.delayTimeout = setTimeout(() => {
            this.searchKey = val;
        }, 300);
    }

    handleDisciplineClick(event) {
        this.selectedDiscipline = event.target.dataset.disc;
    }

    switchToCardView() {
        this.isCardView = true;
    }

    switchToTableView() {
        this.isCardView = false;
    }

    toggleAbstract(event) {
        const id = event.target.dataset.id;
        this.expandedMap = {
            ...this.expandedMap,
            [id]: !this.expandedMap[id]
        };
    }

    handleRefresh() {
        this.isLoading = true;
        refreshApex(this.wiredPapersResult)
            .finally(() => {
                this.isLoading = false;
            });
    }

    handleResetFilters() {
        this.searchKey = '';
        this.selectedDiscipline = 'All';
    }

    stopPropagation(event) {
        event.stopPropagation();
    }

    handleNavigateToPaper(event) {
        const paperId = event.currentTarget.dataset.id;
        this[NavigationMixin.Navigate]({
            type: 'standard__recordPage',
            attributes: {
                recordId: paperId,
                objectApiName: 'Research_Paper__c',
                actionName: 'view'
            }
        });
    }

    handleCopyBibtex(event) {
        event.stopPropagation();
        const paperId = event.currentTarget.dataset.id;
        const paper = this.rawPapers.find(p => p.Id === paperId);
        if (!paper) return;

        const firstAuthorLast = (paper.Authors__c || 'Author').split(',')[0].split(' ').pop().toLowerCase();
        const year = paper.Publication_Year__c || '2024';
        const key = `${firstAuthorLast}${year}`;

        const bibtex = `@article{${key},
  title={${paper.Title__c || ''}},
  author={${paper.Authors__c || ''}},
  journal={${paper.Venue__c || ''}},
  year={${year}},
  doi={${paper.DOI__c || ''}}
}`;

        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(bibtex)
                .then(() => {
                    this.showToast('BibTeX Copied', `Citation for "${paper.Title__c.substring(0, 40)}..." copied to clipboard.`, 'success');
                })
                .catch(() => {
                    this.fallbackCopy(bibtex);
                });
        } else {
            this.fallbackCopy(bibtex);
        }
    }

    fallbackCopy(text) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
            document.execCommand('copy');
            this.showToast('BibTeX Copied', 'Citation copied to clipboard.', 'success');
        } catch (err) {
            this.showToast('Copy Failed', 'Unable to copy citation to clipboard.', 'warning');
        }
        document.body.removeChild(textArea);
    }

    showToast(title, message, variant) {
        this.dispatchEvent(new ShowToastEvent({ title, message, variant }));
    }
}
