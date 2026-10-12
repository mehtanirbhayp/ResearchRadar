import { LightningElement, api, wire, track } from 'lwc';
import getMapPapers from '@salesforce/apex/EreunaController.getMapPapers';
import { refreshApex } from '@salesforce/apex';
import { NavigationMixin } from 'lightning/navigation';

export default class LiteratureCompareMatrix extends NavigationMixin(LightningElement) {
    @api recordId;
    @track isLoading = true;
    @track paperRows = [];
    wiredPapersResult;

    @wire(getMapPapers, { mapId: '$recordId' })
    wiredPapers(result) {
        this.wiredPapersResult = result;
        const { data, error } = result;
        this.isLoading = false;

        if (data) {
            this.paperRows = data.map(link => {
                const p = link.Research_Paper__r || {};
                return {
                    Id: link.Id,
                    paperId: p.Id,
                    title: p.Title__c || 'Untitled Paper',
                    authors: p.Authors__c || 'Unknown Authors',
                    venue: p.Venue__c || 'Preprint / arXiv',
                    year: p.Publication_Year__c || 'N/A',
                    citations: p.Citation_Count__c != null ? p.Citation_Count__c : 0,
                    relevance: link.Relevance_Score__c != null ? link.Relevance_Score__c : 85,
                    rationale: link.Inclusion_Rationale__c || 'Topical relevance to map query',
                    pdfUrl: p.PDF_URL__c,
                    openAccessUrl: p.Open_Access_URL__c
                };
            });
        } else if (error) {
            this.paperRows = [];
        }
    }

    get hasPapers() {
        return this.paperRows && this.paperRows.length > 0;
    }

    handleNavigateToPaper(event) {
        const paperId = event.currentTarget.dataset.id;
        if (!paperId) return;

        this[NavigationMixin.Navigate]({
            type: 'standard__recordPage',
            attributes: {
                recordId: paperId,
                objectApiName: 'Research_Paper__c',
                actionName: 'view'
            }
        });
    }

    async handleRefresh() {
        this.isLoading = true;
        await refreshApex(this.wiredPapersResult);
        this.isLoading = false;
    }

    handleExportCSV() {
        if (!this.paperRows || this.paperRows.length === 0) return;

        let csvContent = 'data:text/csv;charset=utf-8,';
        csvContent += 'Paper Title,Authors,Venue,Year,Citations,Relevance,PDF URL\n';

        this.paperRows.forEach(row => {
            const escapeCsv = (str) => `"${(str || '').toString().replace(/"/g, '""')}"`;
            csvContent += [
                escapeCsv(row.title),
                escapeCsv(row.authors),
                escapeCsv(row.venue),
                row.year,
                row.citations,
                row.relevance + '%',
                escapeCsv(row.pdfUrl || row.openAccessUrl || '')
            ].join(',') + '\n';
        });

        const encodedUri = encodeURI(csvContent);
        const link = document.createElement('a');
        link.setAttribute('href', encodedUri);
        link.setAttribute('download', `Ereuna_Literature_Matrix_${Date.now()}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}
