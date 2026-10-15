import { LightningElement, api, wire, track } from 'lwc';
import getCitationNetwork from '@salesforce/apex/EreunaController.getCitationNetwork';

export default class CitationNetworkGraph extends LightningElement {
    @api recordId;
    @track isLoading = true;
    @track rawNodes = [];
    @track selectedPaperId = null;
    @track sortOrder = 'chronological'; // 'chronological' or 'citations'

    @wire(getCitationNetwork, { mapId: '$recordId' })
    wiredGraph({ data, error }) {
        this.isLoading = false;
        if (data && data.nodes) {
            this.rawNodes = data.nodes || [];
            if (this.rawNodes.length > 0) {
                // Select foundational paper by default
                const sortedByCites = [...this.rawNodes].sort((a, b) => (b.citations || 0) - (a.citations || 0));
                this.selectedPaperId = sortedByCites[0].id;
            }
        } else if (error) {
            this.rawNodes = [];
        }
    }

    get hasData() {
        return this.rawNodes && this.rawNodes.length > 0;
    }

    get foundationalPaper() {
        if (!this.rawNodes || this.rawNodes.length === 0) return null;
        return [...this.rawNodes].sort((a, b) => (b.citations || 0) - (a.citations || 0))[0];
    }

    get totalCitations() {
        if (!this.rawNodes) return 0;
        return this.rawNodes.reduce((sum, p) => sum + (p.citations || 0), 0);
    }

    get yearSpan() {
        if (!this.rawNodes || this.rawNodes.length === 0) return '—';
        const years = this.rawNodes.map(p => p.year || 2024).filter(y => y);
        if (years.length === 0) return '2024';
        const min = Math.min(...years);
        const max = Math.max(...years);
        return min === max ? `${min}` : `${min} – ${max}`;
    }

    get papersList() {
        if (!this.rawNodes || this.rawNodes.length === 0) return [];
        const foundation = this.foundationalPaper;

        let sorted = [...this.rawNodes];
        if (this.sortOrder === 'chronological') {
            sorted.sort((a, b) => {
                const yearDiff = (a.year || 2020) - (b.year || 2020);
                if (yearDiff !== 0) return yearDiff;
                return (b.citations || 0) - (a.citations || 0);
            });
        } else {
            sorted.sort((a, b) => (b.citations || 0) - (a.citations || 0));
        }

        return sorted.map((p, index) => {
            const isBaseline = foundation && foundation.id === p.id;
            const isSelected = this.selectedPaperId === p.id;
            const stepNumber = String(index + 1).padStart(2, '0');

            let lineageRole = isBaseline ? 'Foundational Prior Art' : 'Empirical Benchmark Study';
            let rolePillClass = isBaseline ? 'pill-baseline' : 'pill-benchmark';

            let lineageExplanation = '';
            if (isBaseline) {
                lineageExplanation = 'Seminal baseline publication that defines core protocols, architecture, and baseline measurements for this research area.';
            } else {
                lineageExplanation = `Builds upon prior art (${foundation ? foundation.label : 'baseline'}), directly evaluating optimizations and throughput against baseline metrics.`;
            }

            return {
                ...p,
                stepNumber,
                isBaseline,
                isSelected,
                cardClass: isSelected ? 'timeline-card selected' : 'timeline-card',
                lineageRole,
                rolePillClass,
                lineageExplanation,
                venueText: p.venue || 'Peer-Reviewed Conference / Journal',
                citationsLabel: `${p.citations || 0} Citations`,
                yearText: p.year ? `${p.year}` : '2024'
            };
        });
    }

    get selectedPaper() {
        if (!this.papersList || this.papersList.length === 0) return null;
        const found = this.papersList.find(p => p.id === this.selectedPaperId);
        return found || this.papersList[0];
    }

    get isSortChronological() {
        return this.sortOrder === 'chronological';
    }

    get isSortCitations() {
        return this.sortOrder === 'citations';
    }

    handleSelectPaper(event) {
        this.selectedPaperId = event.currentTarget.dataset.id;
    }

    handleSetChronological() {
        this.sortOrder = 'chronological';
    }

    handleSetCitations() {
        this.sortOrder = 'citations';
    }

    handleResetView() {
        this.sortOrder = 'chronological';
        if (this.foundationalPaper) {
            this.selectedPaperId = this.foundationalPaper.id;
        }
    }
}
