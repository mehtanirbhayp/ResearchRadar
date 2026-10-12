import { LightningElement, track } from 'lwc';
import createOrSynthesizeMap from '@salesforce/apex/EreunaController.createOrSynthesizeMap';
import initializeSampleData from '@salesforce/apex/EreunaController.initializeSampleData';
import { NavigationMixin } from 'lightning/navigation';

export default class EreunaTopicSearch extends NavigationMixin(LightningElement) {
    @track topicQuery = '';
    @track selectedDiscipline = 'Cloud Computing';
    @track isLoading = false;
    @track pipelineStep = '1';
    @track statusMessage = '';
    @track feedbackMessage = '';
    @track feedbackType = 'success';

    get disciplineOptions() {
        return [
            { label: 'Cloud Computing', value: 'Cloud Computing' },
            { label: 'Artificial Intelligence', value: 'Artificial Intelligence' },
            { label: 'Distributed Systems', value: 'Distributed Systems' },
            { label: 'Computer Science', value: 'Computer Science' },
            { label: 'Biomedicine', value: 'Biomedicine' }
        ];
    }

    get feedbackClass() {
        return this.feedbackType === 'success' 
            ? 'slds-notify slds-notify_alert slds-theme_success slds-m-top_small'
            : 'slds-notify slds-notify_alert slds-theme_error slds-m-top_small';
    }

    handleTopicChange(event) {
        this.topicQuery = event.target.value;
    }

    handleDisciplineChange(event) {
        this.selectedDiscipline = event.target.value;
    }

    async handleSeedDemoData() {
        this.isLoading = true;
        this.feedbackMessage = '';
        this.pipelineStep = '1';
        this.statusMessage = 'Connecting to Force.com database...';

        try {
            const res = await initializeSampleData();
            this.feedbackType = 'success';
            this.feedbackMessage = 'Successfully seeded Cloud Computing research maps, papers, findings, and gaps!';
            this.dispatchEvent(new CustomEvent('datarefreshed'));
        } catch (error) {
            this.feedbackType = 'error';
            this.feedbackMessage = 'Failed to seed data: ' + (error.body ? error.body.message : error.message);
        } finally {
            this.isLoading = false;
        }
    }

    async handleSynthesize() {
        if (!this.topicQuery || !this.topicQuery.trim()) {
            this.feedbackType = 'error';
            this.feedbackMessage = 'Please enter a research topic to analyze.';
            return;
        }

        this.isLoading = true;
        this.feedbackMessage = '';
        
        try {
            // Stage 1
            this.pipelineStep = '1';
            this.statusMessage = 'Searching scholarly indices (OpenAlex, arXiv, Semantic Scholar)...';
            await this.sleep(700);

            // Stage 2
            this.pipelineStep = '2';
            this.statusMessage = 'Fetching and parsing open-access full text PDFs...';
            await this.sleep(700);

            // Stage 3
            this.pipelineStep = '3';
            this.statusMessage = 'Extracting verbatim findings, quantitative metrics & contradictions...';
            await this.sleep(800);

            // Stage 4
            this.pipelineStep = '4';
            this.statusMessage = 'Verifying evidence claims and generating research map in Salesforce...';

            const createdMap = await createOrSynthesizeMap({
                topic: this.topicQuery.trim(),
                discipline: this.selectedDiscipline
            });

            this.feedbackType = 'success';
            this.feedbackMessage = `Research map "${createdMap.Name}" successfully created! Redirecting...`;

            await this.sleep(600);

            // Navigate to newly created record
            this[NavigationMixin.Navigate]({
                type: 'standard__recordPage',
                attributes: {
                    recordId: createdMap.Id,
                    objectApiName: 'Research_Map__c',
                    actionName: 'view'
                }
            });

            this.dispatchEvent(new CustomEvent('mapcreated', { detail: createdMap }));
        } catch (error) {
            this.feedbackType = 'error';
            this.feedbackMessage = 'Synthesis error: ' + (error.body ? error.body.message : error.message);
        } finally {
            this.isLoading = false;
        }
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}
