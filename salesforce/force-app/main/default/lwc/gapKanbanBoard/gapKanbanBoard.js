import { LightningElement, track, wire } from 'lwc';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import { refreshApex } from '@salesforce/apex';
import getAllGaps from '@salesforce/apex/EreunaController.getAllGaps';
import getRecentMaps from '@salesforce/apex/EreunaController.getRecentMaps';
import updateGapStatus from '@salesforce/apex/EreunaController.updateGapStatus';
import createResearchGap from '@salesforce/apex/EreunaController.createResearchGap';

export default class GapKanbanBoard extends LightningElement {
    @track selectedMapId = null;
    @track isLoading = true;
    @track isModalOpen = false;
    @track isSaving = false;

    // Modal fields
    @track newGapMapId = '';
    @track newGapProblem = '';
    @track newGapExperiment = '';
    @track newGapPriority = 'High';
    @track newGapComplexity = 'Medium';

    rawGaps = [];
    rawMaps = [];
    wiredGapsResult;

    priorityOptions = [
        { label: 'High Priority', value: 'High' },
        { label: 'Medium Priority', value: 'Medium' },
        { label: 'Low Priority', value: 'Low' }
    ];

    complexityOptions = [
        { label: 'High Complexity', value: 'High' },
        { label: 'Medium Complexity', value: 'Medium' },
        { label: 'Low Complexity', value: 'Low' }
    ];

    @wire(getRecentMaps, { discipline: 'All' })
    wiredMaps({ data, error }) {
        if (data) {
            this.rawMaps = data;
        }
    }

    @wire(getAllGaps, { mapId: '$selectedMapId' })
    wiredGaps(result) {
        this.wiredGapsResult = result;
        const { data, error } = result;
        if (data) {
            this.rawGaps = data;
            this.isLoading = false;
        } else if (error) {
            this.isLoading = false;
            this.showToast('Error', 'Unable to load research gaps.', 'error');
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

    get createMapOptions() {
        if (!this.rawMaps) return [];
        return this.rawMaps.map(m => ({ label: m.Topic__c, value: m.Id }));
    }

    get formattedGaps() {
        if (!this.rawGaps) return [];
        return this.rawGaps.map(gap => {
            let priorityClass = 'priority-badge priority-med';
            if (gap.Priority__c === 'High') priorityClass = 'priority-badge priority-high';
            else if (gap.Priority__c === 'Low') priorityClass = 'priority-badge priority-low';

            return {
                ...gap,
                priorityClass,
                topicTitle: gap.Research_Map__r ? gap.Research_Map__r.Topic__c : 'General Cloud Systems'
            };
        });
    }

    get identifiedList() {
        return this.formattedGaps.filter(g => g.Status__c === 'Identified');
    }

    get inReviewList() {
        return this.formattedGaps.filter(g => g.Status__c === 'In Review');
    }

    get draftedList() {
        return this.formattedGaps.filter(g => g.Status__c === 'Experiment Drafted');
    }

    get addressedList() {
        return this.formattedGaps.filter(g => g.Status__c === 'Addressed');
    }

    get isIdentifiedEmpty() {
        return this.identifiedList.length === 0;
    }

    get isInReviewEmpty() {
        return this.inReviewList.length === 0;
    }

    get isDraftedEmpty() {
        return this.draftedList.length === 0;
    }

    get isAddressedEmpty() {
        return this.addressedList.length === 0;
    }

    get totalGapsCount() {
        return this.formattedGaps.length;
    }

    handleMapFilterChange(event) {
        this.selectedMapId = event.detail.value || null;
        this.isLoading = true;
    }

    handleRefresh() {
        this.isLoading = true;
        refreshApex(this.wiredGapsResult).finally(() => {
            this.isLoading = false;
        });
    }

    handleMoveStage(event) {
        const gapId = event.target.dataset.id;
        const newStatus = event.target.dataset.target;
        if (!gapId || !newStatus) return;

        // Optimistic UI update
        const updated = this.rawGaps.map(g => {
            if (g.Id === gapId) {
                return { ...g, Status__c: newStatus };
            }
            return g;
        });
        this.rawGaps = updated;

        updateGapStatus({ gapId, newStatus })
            .then(() => {
                this.showToast('Milestone Updated', `Moved research gap to "${newStatus}".`, 'success');
                return refreshApex(this.wiredGapsResult);
            })
            .catch(error => {
                this.showToast('Error', error.body?.message || 'Failed to update gap stage.', 'error');
                refreshApex(this.wiredGapsResult);
            });
    }

    openCreateModal() {
        if (this.rawMaps && this.rawMaps.length > 0) {
            this.newGapMapId = this.selectedMapId || this.rawMaps[0].Id;
        }
        this.isModalOpen = true;
    }

    closeCreateModal() {
        this.isModalOpen = false;
        this.newGapProblem = '';
        this.newGapExperiment = '';
    }

    handleNewMapChange(e) { this.newGapMapId = e.detail.value; }
    handleNewProblemChange(e) { this.newGapProblem = e.detail.value; }
    handleNewExperimentChange(e) { this.newGapExperiment = e.detail.value; }
    handleNewPriorityChange(e) { this.newGapPriority = e.detail.value; }
    handleNewComplexityChange(e) { this.newGapComplexity = e.detail.value; }

    handleSaveNewGap() {
        if (!this.newGapMapId || !this.newGapProblem) {
            this.showToast('Missing Fields', 'Please select a Research Map and provide a Problem Statement.', 'warning');
            return;
        }
        this.isSaving = true;
        createResearchGap({
            mapId: this.newGapMapId,
            problem: this.newGapProblem,
            experiment: this.newGapExperiment,
            priority: this.newGapPriority,
            complexity: this.newGapComplexity
        })
            .then(newGap => {
                this.showToast('Gap Added', 'New research challenge added to Kanban board!', 'success');
                this.closeCreateModal();
                return refreshApex(this.wiredGapsResult);
            })
            .catch(error => {
                this.showToast('Error', error.body?.message || 'Failed to create gap.', 'error');
            })
            .finally(() => {
                this.isSaving = false;
            });
    }

    showToast(title, message, variant) {
        this.dispatchEvent(new ShowToastEvent({ title, message, variant }));
    }
}
