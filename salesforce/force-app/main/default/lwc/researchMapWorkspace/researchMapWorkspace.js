import { LightningElement, api, wire, track } from 'lwc';
import getMapDetails from '@salesforce/apex/EreunaController.getMapDetails';
import getMapFindings from '@salesforce/apex/EreunaController.getMapFindings';
import getMapConflicts from '@salesforce/apex/EreunaController.getMapConflicts';

export default class ResearchMapWorkspace extends LightningElement {
    @api recordId;

    @track mapDetails;
    @track rawFindings = [];
    @track rawConflicts = [];

    @wire(getMapDetails, { mapId: '$recordId' })
    wiredDetails({ data, error }) {
        if (data) {
            this.mapDetails = data;
        }
    }

    @wire(getMapFindings, { mapId: '$recordId' })
    wiredFindings({ data, error }) {
        if (data) {
            this.rawFindings = data;
        }
    }

    @wire(getMapConflicts, { mapId: '$recordId' })
    wiredConflicts({ data, error }) {
        if (data) {
            this.rawConflicts = data;
        }
    }

    get topicTitle() {
        return this.mapDetails?.Topic__c || 'Research Synthesis Map';
    }

    get targetDiscipline() {
        return this.mapDetails?.Target_Discipline__c || 'Cloud Computing';
    }

    get mapStatus() {
        return this.mapDetails?.Status__c || 'Synthesized';
    }

    get totalPapers() {
        return this.mapDetails?.Total_Papers__c || 0;
    }

    get totalFindings() {
        return this.mapDetails?.Total_Findings__c || 0;
    }

    get totalGaps() {
        return this.mapDetails?.Total_Gaps__c || 0;
    }

    get totalConflicts() {
        return this.mapDetails?.Total_Conflicts__c || 0;
    }

    get synthesisSummary() {
        return this.mapDetails?.Synthesis_Summary__c || null;
    }

    get findingsList() {
        if (!this.rawFindings) return [];
        return this.rawFindings.map(f => ({
            ...f,
            paperTitle: f.Research_Paper__r?.Title__c || 'Academic Source',
            paperYear: f.Research_Paper__r?.Publication_Year__c || '2024'
        }));
    }

    get hasFindings() {
        return this.findingsList && this.findingsList.length > 0;
    }

    get conflictsList() {
        if (!this.rawConflicts) return [];
        return this.rawConflicts.map(c => ({
            ...c,
            paperATitle: c.Paper_A__r?.Title__c || 'Study A',
            paperBTitle: c.Paper_B__r?.Title__c || 'Study B'
        }));
    }

    get hasConflicts() {
        return this.conflictsList && this.conflictsList.length > 0;
    }
}
