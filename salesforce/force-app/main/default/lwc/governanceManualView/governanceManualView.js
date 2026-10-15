import { LightningElement, track } from 'lwc';

export default class GovernanceManualView extends LightningElement {
    @track activeTab = 'manual';

    get isTabManual() {
        return this.activeTab === 'manual';
    }

    get isTabTerms() {
        return this.activeTab === 'terms';
    }

    get isTabDisclaimer() {
        return this.activeTab === 'disclaimer';
    }

    get isTabSources() {
        return this.activeTab === 'sources';
    }

    get isTabRegulations() {
        return this.activeTab === 'regulations';
    }

    get navManualClass() {
        return this.activeTab === 'manual' ? 'tab-btn active' : 'tab-btn';
    }

    get navTermsClass() {
        return this.activeTab === 'terms' ? 'tab-btn active' : 'tab-btn';
    }

    get navDisclaimerClass() {
        return this.activeTab === 'disclaimer' ? 'tab-btn active' : 'tab-btn';
    }

    get navSourcesClass() {
        return this.activeTab === 'sources' ? 'tab-btn active' : 'tab-btn';
    }

    get navRegulationsClass() {
        return this.activeTab === 'regulations' ? 'tab-btn active' : 'tab-btn';
    }

    handleSwitchTab(event) {
        this.activeTab = event.currentTarget.dataset.tab;
    }
}
