import { LightningElement, track, wire } from 'lwc';
import { NavigationMixin } from 'lightning/navigation';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import getRecentMaps from '@salesforce/apex/EreunaController.getRecentMaps';
import createOrSynthesizeMap from '@salesforce/apex/EreunaController.createOrSynthesizeMap';
import { refreshApex } from '@salesforce/apex';

export default class MapExplorer extends NavigationMixin(LightningElement) {
    @track searchKey = '';
    @track selectedDiscipline = 'All';
    @track isLoading = true;
    @track isModalOpen = false;
    @track isSynthesizing = false;

    @track newTopic = '';
    @track newDiscipline = 'Cloud Computing';

    rawMaps = [];
    wiredMapsResult;

    disciplineOptions = [
        { label: 'Cloud Computing', value: 'Cloud Computing' },
        { label: 'Distributed Systems', value: 'Distributed Systems' },
        { label: 'Artificial Intelligence', value: 'Artificial Intelligence' },
        { label: 'Computer Science', value: 'Computer Science' }
    ];

    @wire(getRecentMaps, { discipline: '$selectedDiscipline' })
    wiredMaps(result) {
        this.wiredMapsResult = result;
        const { data, error } = result;
        if (data) {
            this.rawMaps = data;
            this.isLoading = false;
        } else if (error) {
            this.isLoading = false;
            this.showToast('Error', 'Unable to fetch research maps.', 'error');
        }
    }

    get filteredMaps() {
        if (!this.rawMaps) return [];
        let list = this.rawMaps;
        if (this.searchKey && this.searchKey.trim() !== '') {
            const key = this.searchKey.toLowerCase();
            list = list.filter(m => 
                (m.Topic__c && m.Topic__c.toLowerCase().includes(key)) ||
                (m.Synthesis_Summary__c && m.Synthesis_Summary__c.toLowerCase().includes(key))
            );
        }
        return list.map(m => {
            let statusClass = 'status-tag status-draft slds-m-left_x-small';
            if (m.Status__c === 'Synthesized') statusClass = 'status-tag status-syn slds-m-left_x-small';
            else if (m.Status__c === 'In Progress') statusClass = 'status-tag status-prog slds-m-left_x-small';

            return {
                ...m,
                statusClass
            };
        });
    }

    get hasMaps() {
        return this.filteredMaps && this.filteredMaps.length > 0;
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

    handleSearchChange(event) {
        this.searchKey = event.target.value;
    }

    handleDisciplineClick(event) {
        this.selectedDiscipline = event.target.dataset.disc;
        this.isLoading = true;
    }

    handleRefresh() {
        this.isLoading = true;
        refreshApex(this.wiredMapsResult).finally(() => {
            this.isLoading = false;
        });
    }

    handleLaunchWorkspace(event) {
        const mapId = event.currentTarget.dataset.id;
        this[NavigationMixin.Navigate]({
            type: 'standard__recordPage',
            attributes: {
                recordId: mapId,
                objectApiName: 'Research_Map__c',
                actionName: 'view'
            }
        });
    }

    handleNavigateToRecord(event) {
        this.handleLaunchWorkspace(event);
    }

    openSynthesizeModal() {
        this.isModalOpen = true;
    }

    closeSynthesizeModal() {
        this.isModalOpen = false;
        this.newTopic = '';
    }

    handleNewTopicChange(e) { this.newTopic = e.target.value; }
    handleNewDisciplineChange(e) { this.newDiscipline = e.detail.value; }

    handleSynthesizeSubmit() {
        if (!this.newTopic || this.newTopic.trim() === '') {
            this.showToast('Topic Required', 'Please enter a topic title.', 'warning');
            return;
        }
        this.isSynthesizing = true;
        createOrSynthesizeMap({ topic: this.newTopic, discipline: this.newDiscipline })
            .then(newMap => {
                this.showToast('Synthesis Complete', `Created research map for "${this.newTopic}".`, 'success');
                this.closeSynthesizeModal();
                return refreshApex(this.wiredMapsResult);
            })
            .catch(err => {
                this.showToast('Error', err.body?.message || 'Failed to synthesize map.', 'error');
            })
            .finally(() => {
                this.isSynthesizing = false;
            });
    }

    showToast(title, message, variant) {
        this.dispatchEvent(new ShowToastEvent({ title, message, variant }));
    }
}
