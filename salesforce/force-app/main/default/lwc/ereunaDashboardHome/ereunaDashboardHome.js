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

    get hasRecentMaps() {
        return this.rawMaps && this.rawMaps.length > 0;
    }

    get recentMaps() {
        return this.rawMaps.map(m => {
            let statusClass = 'tag-pill-subtle';
            if (m.Status__c === 'Synthesized') statusClass = 'tag-pill';
            return {
                ...m,
                statusClass
            };
        });
    }

    get mapsList() {
        return this.recentMaps;
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

    get filterAllClass() {
        return this.selectedDiscipline === 'All' ? 'filter-pill active' : 'filter-pill';
    }

    get filterChemClass() {
        return this.selectedDiscipline === 'Chemical Engineering' ? 'filter-pill active' : 'filter-pill';
    }

    get filterMechClass() {
        return this.selectedDiscipline === 'Mechanical Engineering' ? 'filter-pill active' : 'filter-pill';
    }

    get filterCivilClass() {
        return this.selectedDiscipline === 'Civil Engineering' ? 'filter-pill active' : 'filter-pill';
    }

    get filterEeeClass() {
        return this.selectedDiscipline === 'Electrical & Electronics (EEE)' ? 'filter-pill active' : 'filter-pill';
    }

    get filterEceClass() {
        return this.selectedDiscipline === 'Electronics & Communication (ECE)' ? 'filter-pill active' : 'filter-pill';
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

    handleMapSynthesized() {
        this.handleDataRefreshed();
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

    @track isGovernanceModalOpen = false;
    @track activeGovernanceTab = 'manual';

    get isTabManual() {
        return this.activeGovernanceTab === 'manual';
    }

    get isTabTerms() {
        return this.activeGovernanceTab === 'terms';
    }

    get isTabDisclaimer() {
        return this.activeGovernanceTab === 'disclaimer';
    }

    get isTabSources() {
        return this.activeGovernanceTab === 'sources';
    }

    get isTabRegulations() {
        return this.activeGovernanceTab === 'regulations';
    }

    get navManualClass() {
        return this.activeGovernanceTab === 'manual' ? 'gov-nav-tab active' : 'gov-nav-tab';
    }

    get navTermsClass() {
        return this.activeGovernanceTab === 'terms' ? 'gov-nav-tab active' : 'gov-nav-tab';
    }

    get navDisclaimerClass() {
        return this.activeGovernanceTab === 'disclaimer' ? 'gov-nav-tab active' : 'gov-nav-tab';
    }

    get navSourcesClass() {
        return this.activeGovernanceTab === 'sources' ? 'gov-nav-tab active' : 'gov-nav-tab';
    }

    get navRegulationsClass() {
        return this.activeGovernanceTab === 'regulations' ? 'gov-nav-tab active' : 'gov-nav-tab';
    }

    handleOpenManual() {
        this.activeGovernanceTab = 'manual';
        this.isGovernanceModalOpen = true;
    }

    handleOpenTerms() {
        this.activeGovernanceTab = 'terms';
        this.isGovernanceModalOpen = true;
    }

    handleOpenDisclaimer() {
        this.activeGovernanceTab = 'disclaimer';
        this.isGovernanceModalOpen = true;
    }

    handleOpenSources() {
        this.activeGovernanceTab = 'sources';
        this.isGovernanceModalOpen = true;
    }

    handleOpenRegulations() {
        this.activeGovernanceTab = 'regulations';
        this.isGovernanceModalOpen = true;
    }

    handleSwitchModalTab(event) {
        this.activeGovernanceTab = event.currentTarget.dataset.tab;
    }

    handleCloseGovernanceModal() {
        this.isGovernanceModalOpen = false;
    }

    handleNavigateToPapers() {
        this[NavigationMixin.Navigate]({
            type: 'standard__navItemPage',
            attributes: { apiName: 'Paper_Explorer' }
        });
    }

    handleNavigateToGaps() {
        this[NavigationMixin.Navigate]({
            type: 'standard__navItemPage',
            attributes: { apiName: 'Gap_Board' }
        });
    }

    handleNavigateToMaps() {
        this[NavigationMixin.Navigate]({
            type: 'standard__navItemPage',
            attributes: { apiName: 'Research_Map_Hub' }
        });
    }

    handleNavigateToFindings() {
        this[NavigationMixin.Navigate]({
            type: 'standard__navItemPage',
            attributes: { apiName: 'Findings_Explorer' }
        });
    }
}
