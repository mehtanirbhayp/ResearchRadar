import { LightningElement, api, wire, track } from 'lwc';
import getCitationNetwork from '@salesforce/apex/EreunaController.getCitationNetwork';

export default class CitationNetworkGraph extends LightningElement {
    @api recordId;
    @track isLoading = true;
    @track rawNodes = [];
    @track rawLinks = [];
    @track selectedNode = null;

    @wire(getCitationNetwork, { mapId: '$recordId' })
    wiredGraph({ data, error }) {
        this.isLoading = false;
        if (data) {
            this.rawNodes = data.nodes || [];
            this.rawLinks = data.links || [];
            if (this.rawNodes.length > 0) {
                this.selectedNode = this.rawNodes[0];
            }
        } else if (error) {
            this.rawNodes = [];
            this.rawLinks = [];
        }
    }

    get hasGraphData() {
        return this.rawNodes && this.rawNodes.length > 0;
    }

    get renderNodes() {
        const count = this.rawNodes.length;
        if (count === 0) return [];

        const centerX = 350;
        const centerY = 225;
        const radiusLayout = Math.min(centerX - 90, centerY - 50);

        return this.rawNodes.map((node, i) => {
            const angle = (2 * Math.PI * i) / count - Math.PI / 2;
            const x = centerX + radiusLayout * Math.cos(angle);
            const y = centerY + radiusLayout * Math.sin(angle);

            // Radius scaled by citation count
            const r = Math.min(38, Math.max(22, 22 + (node.citations || 0) / 10));

            const isSelected = this.selectedNode && this.selectedNode.id === node.id;
            const circleClass = isSelected ? 'node-circle selected' : 'node-circle';

            // Shortened label for SVG
            const shortLabel = (node.label && node.label.length > 18) 
                ? node.label.substring(0, 16) + '...' 
                : (node.label || 'Paper');

            return {
                ...node,
                x,
                y,
                radius: r,
                textY: y + 4,
                subTextY: y + r + 14,
                shortLabel,
                circleClass
            };
        });
    }

    get renderLinks() {
        const nodes = this.renderNodes;
        const nodeMap = new Map();
        nodes.forEach(n => nodeMap.set(n.id, n));

        return this.rawLinks.map((link, idx) => {
            const src = nodeMap.get(link.source);
            const tgt = nodeMap.get(link.target);
            if (src && tgt) {
                return {
                    id: `link-${idx}`,
                    x1: src.x,
                    y1: src.y,
                    x2: tgt.x,
                    y2: tgt.y,
                    dash: '0'
                };
            }
            return null;
        }).filter(l => l !== null);
    }

    handleNodeClick(event) {
        const nodeId = event.currentTarget.dataset.id;
        const found = this.rawNodes.find(n => n.id === nodeId);
        if (found) {
            this.selectedNode = found;
        }
    }

    handleResetView() {
        if (this.rawNodes.length > 0) {
            this.selectedNode = this.rawNodes[0];
        }
    }
}
