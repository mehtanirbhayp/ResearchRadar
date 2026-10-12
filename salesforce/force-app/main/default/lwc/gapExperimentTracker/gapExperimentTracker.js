import { LightningElement, api, wire, track } from 'lwc';
import getMapGaps from '@salesforce/apex/EreunaController.getMapGaps';
import updateGapStatus from '@salesforce/apex/EreunaController.updateGapStatus';
import { refreshApex } from '@salesforce/apex';

export default class GapExperimentTracker extends LightningElement {
    @api recordId;
    @track isLoading = true;
    @track gaps = [];
    wiredGapsResult;

    @wire(getMapGaps, { mapId: '$recordId' })
    wiredGaps(result) {
        this.wiredGapsResult = result;
        const { data, error } = result;
        this.isLoading = false;

        if (data) {
            this.gaps = data;
        } else if (error) {
            this.gaps = [];
        }
    }

    get hasGaps() {
        return this.gaps && this.gaps.length > 0;
    }

    get gapCards() {
        return this.gaps.map(g => {
            const isHigh = g.Priority__c === 'High';
            const isMedium = g.Priority__c === 'Medium';
            let priorityBadgeClass = 'slds-badge slds-theme_default';
            if (isHigh) priorityBadgeClass = 'slds-badge slds-theme_error';
            else if (isMedium) priorityBadgeClass = 'slds-badge slds-theme_warning';

            return {
                ...g,
                priorityBadgeClass,
                isInReview: g.Status__c === 'In Review',
                isDrafted: g.Status__c === 'Experiment Drafted',
                isAddressed: g.Status__c === 'Addressed'
            };
        });
    }

    async handleStatusChange(event) {
        const gapId = event.currentTarget.dataset.id;
        const newStatus = event.currentTarget.dataset.status;

        if (!gapId || !newStatus) return;

        this.isLoading = true;
        try {
            await updateGapStatus({ gapId, newStatus });
            await refreshApex(this.wiredGapsResult);
        } catch (error) {
            console.error('Failed to update gap status', error);
        } finally {
            this.isLoading = false;
        }
    }

    async handleRefresh() {
        this.isLoading = true;
        await refreshApex(this.wiredGapsResult);
        this.isLoading = false;
    }
}
