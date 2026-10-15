import { LightningElement, track, wire } from 'lwc';
import { NavigationMixin } from 'lightning/navigation';
import getMapFindings from '@salesforce/apex/EreunaController.getMapFindings';
import getRecentMaps from '@salesforce/apex/EreunaController.getRecentMaps';
import { refreshApex } from '@salesforce/apex';

export default class FindingsExplorer extends NavigationMixin(LightningElement) {
    @track searchKey = '';
    @track selectedMapId = null;
    @track selectedStatus = 'All';
    @track isLoading = true;

    rawFindings = [];
    rawMaps = [];
    wiredFindingsResult;

    @wire(getRecentMaps, { discipline: 'All' })
    wiredMaps({ data }) {
        if (data) {
            this.rawMaps = data;
        }
    }

    @wire(getMapFindings, { mapId: '$selectedMapId' })
    wiredFindings(result) {
        this.wiredFindingsResult = result;
        const { data, error } = result;
        if (data) {
            this.rawFindings = data;
            this.isLoading = false;
        } else if (error) {
            this.isLoading = false;
        }
    }

    get mapOptions() {
        const opts = [{ label: 'All Research Topics', value: null }];
        if (this.rawMaps) {
            this.rawMaps.forEach(m => {
                opts.push({ label: m.Topic__c, value: m.Id });
            });
        }
        return opts;
    }

    get filteredFindings() {
        if (!this.rawFindings) return [];
        let list = this.rawFindings;

        if (this.selectedStatus !== 'All') {
            list = list.filter(f => f.Verification_Status__c === this.selectedStatus);
        }

        if (this.searchKey && this.searchKey.trim() !== '') {
            const key = this.searchKey.toLowerCase();
            list = list.filter(f =>
                (f.Claim_Summary__c && f.Claim_Summary__c.toLowerCase().includes(key)) ||
                (f.Exact_Quote__c && f.Exact_Quote__c.toLowerCase().includes(key)) ||
                (f.Research_Paper__r && f.Research_Paper__r.Title__c && f.Research_Paper__r.Title__c.toLowerCase().includes(key))
            );
        }

        return list.map(f => {
            let statusClass = 'status-badge status-ver';
            if (f.Verification_Status__c === 'Extracted') statusClass = 'status-badge status-ext';
            else if (f.Verification_Status__c === 'Disputed') statusClass = 'status-badge status-disp';

            return {
                ...f,
                statusClass,
                paperTitle: f.Research_Paper__r?.Title__c || 'Academic Paper',
                paperYear: f.Research_Paper__r?.Publication_Year__c || '2024',
                paperId: f.Research_Paper__r?.Id,
                topicTitle: f.Research_Map__r?.Topic__c || 'Cloud Computing'
            };
        });
    }

    get hasFindings() {
        return this.filteredFindings && this.filteredFindings.length > 0;
    }

    get totalCountLabel() {
        return `${this.filteredFindings.length} Claims Verified`;
    }

    get statusAllVariant() {
        return this.selectedStatus === 'All' ? 'brand' : 'neutral';
    }

    get statusVerVariant() {
        return this.selectedStatus === 'Verified' ? 'brand' : 'neutral';
    }

    handleSearchChange(e) {
        this.searchKey = e.target.value;
    }

    handleMapChange(e) {
        this.selectedMapId = e.detail.value || null;
        this.isLoading = true;
    }

    handleStatusFilter(e) {
        this.selectedStatus = e.target.dataset.status;
    }

    handleRefresh() {
        this.isLoading = true;
        refreshApex(this.wiredFindingsResult).finally(() => {
            this.isLoading = false;
        });
    }

    handleNavigateToPaper(e) {
        const paperId = e.target.dataset.id;
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
}
