import { LightningElement, track, wire } from 'lwc';
import getRecentMaps from '@salesforce/apex/EreunaController.getRecentMaps';
import { refreshApex } from '@salesforce/apex';
import { NavigationMixin } from 'lightning/navigation';

export default class EreunaDashboardHome extends NavigationMixin(LightningElement) {
    @track selectedDiscipline = 'All';
    @track isLoading = true;
    @track rawMaps = [];
    wiredMapsResult;

    @wire(getRecentMaps, { discipline: '$selectedDiscipline' })
    wiredMaps(result) {
        this.wiredMapsResult = result;
        const { data, error } = result;
        this.isLoading = false;

        if (data) {
            this.rawMaps = data;
        } else if (error) {
            this.rawMaps = [];
        }
    }

    get hasMaps() {
        return this.rawMaps && this.rawMaps.length > 0;
    }

    get mapsList() {
        return this.rawMaps.map(m => {
            let statusClass = 'slds-badge slds-badge_lightest';
            if (m.Status__c === 'Synthesized') statusClass = 'slds-badge slds-theme_success';
            else if (m.Status__c === 'In Progress') statusClass = 'slds-badge slds-theme_warning';

            return {
                ...m,
                statusClass
            };
        });
    }

    get totalMapsCount() {
        return this.rawMaps.length;
    }

    get totalPapersCount() {
        return this.rawMaps.reduce((acc, m) => acc + (m.Total_Papers__c || 0), 0);
    }

    get totalFindingsCount() {
        return this.rawMaps.reduce((acc, m) => acc + (m.Total_Findings__c || 0), 0);
    }

    get totalGapsCount() {
        return this.rawMaps.reduce((acc, m) => acc + (m.Total_Gaps__c || 0), 0);
    }

    get filterAllVariant() {
        return this.selectedDiscipline === 'All' ? 'brand' : 'neutral';
    }

    get filterCloudVariant() {
        return this.selectedDiscipline === 'Cloud Computing' ? 'brand' : 'neutral';
    }

    get filterDistVariant() {
        return this.selectedDiscipline === 'Distributed Systems' ? 'brand' : 'neutral';
    }

    handleFilterChange(event) {
        this.selectedDiscipline = event.currentTarget.dataset.disc;
        this.isLoading = true;
    }

    async handleDataRefreshed() {
        this.isLoading = true;
        await refreshApex(this.wiredMapsResult);
        this.isLoading = false;
    }

    handleNavigateToMap(event) {
        const mapId = event.currentTarget.dataset.id;
        if (!mapId) return;

        this[NavigationMixin.Navigate]({
            type: 'standard__recordPage',
            attributes: {
                recordId: mapId,
                objectApiName: 'Research_Map__c',
                actionName: 'view'
            }
        });
    }
}
