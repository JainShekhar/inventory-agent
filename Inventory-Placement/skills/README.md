# Supply Chain Skills for AI Coding Assistants

A comprehensive collection of 132 AI agent skills focused on supply chain management tasks. Built for supply chain professionals, operations researchers, and logistics managers who want AI coding assistants (Claude Code, Cursor, GitHub Copilot, etc.) to help with optimization, forecasting, network design, inventory management, and operations research.

**🎉 NEW: Now available as a Claude Code plugin!** Install once and get instant access to all 132 supply chain skills in your coding CLI.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your AI coding assistant can recognize when you're working on a supply chain problem and apply the right frameworks, algorithms, and best practices.

## 🚀 Quick Start - Plugin Installation

This repository is now configured as a **Claude Code plugin** for seamless integration with AI coding assistants.

### For Claude Code CLI

```bash
# Clone the repository
git clone https://github.com/kishorkukreja/awesome-supply-chain.git
cd awesome-supply-chain

# Install all skills to Claude Code
cp -r skills/* ~/.claude/skills/

# Or install specific skills only
cp -r skills/demand-forecasting ~/.claude/skills/
cp -r skills/vehicle-routing-problem ~/.claude/skills/
cp -r skills/inventory-optimization ~/.claude/skills/
```

### For Other AI Assistants

**Cursor, Aider, Continue, or other IDEs:**
Copy the `skills/` directory contents to your AI assistant's custom skills or instructions folder. Each skill is a standalone markdown file that works with any AI coding assistant that supports custom instructions.

### Using as a Git Submodule

```bash
# Add as submodule to your project
cd your-project
git submodule add https://github.com/kishorkukreja/awesome-supply-chain.git

# Symlink skills to Claude Code
ln -s $(pwd)/awesome-supply-chain/skills/* ~/.claude/skills/
```

## Overview

This repository contains **132 comprehensive skills** covering:
- **Core Supply Chain Functions** (45 skills)
- **Domain-Specific Verticals** (34 skills)
- **Operations Research Problems** (43 skills)
- **Advanced Optimization & AI** (10 skills)

Each skill includes:
- Expert frameworks and methodologies
- Working Python code implementations
- Optimization algorithms and models
- Real-world problem-solving approaches
- Tools and library recommendations
- Common challenges and solutions

---

## 📚 Skills by Category

### **1. Planning & Forecasting** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [demand-forecasting](demand-forecasting/) | Time series forecasting, ML models, demand sensing | "forecast demand," "predict sales," "time series," "MAPE" |
| [network-design](network-design/) | DC location, distribution network optimization | "network design," "facility location," "DC location" |
| [scenario-planning](scenario-planning/) | What-if analysis, Monte Carlo, risk scenarios | "scenario planning," "what-if," "sensitivity analysis" |
| [capacity-planning](capacity-planning/) | Production capacity, bottleneck analysis, OEE | "capacity planning," "bottleneck," "OEE" |
| [sales-operations-planning](sales-operations-planning/) | S&OP process, consensus planning, IBP | "S&OP," "sales and operations," "IBP" |
| [master-production-scheduling](master-production-scheduling/) | MPS, ATP, time fences, rough-cut capacity | "MPS," "available to promise," "master schedule" |

---

### **2. Inventory & Warehousing** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [inventory-optimization](inventory-optimization/) | EOQ, safety stock, reorder points, service levels | "inventory optimization," "safety stock," "EOQ" |
| [warehouse-design](warehouse-design/) | Layout optimization, slotting, space utilization | "warehouse design," "layout," "slotting" |
| [order-fulfillment](order-fulfillment/) | Pick strategies, packing, carrier selection | "order fulfillment," "picking," "pack-and-ship" |
| [replenishment-strategy](replenishment-strategy/) | Min-max, DRP, VMI, pull systems | "replenishment," "min-max," "VMI" |
| [cycle-counting](cycle-counting/) | ABC counting, variance analysis, accuracy | "cycle counting," "inventory accuracy" |
| [warehouse-automation](warehouse-automation/) | AS/RS, AMR, automation ROI, goods-to-person | "warehouse automation," "AS/RS," "AMR," "robotics" |

---

### **3. Transportation & Logistics** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [route-optimization](route-optimization/) | VRP, TSP, delivery routing, Google OR-Tools | "route optimization," "VRP," "delivery routes" |
| [fleet-management](fleet-management/) | Fleet sizing, TCO, utilization, maintenance | "fleet management," "fleet sizing," "TCO" |
| [last-mile-delivery](last-mile-delivery/) | Urban logistics, delivery density, micro-fulfillment | "last mile," "delivery density," "dark stores" |
| [freight-optimization](freight-optimization/) | Mode selection, LTL vs. TL, consolidation | "freight optimization," "LTL," "mode selection" |
| [cross-docking](cross-docking/) | Flow-through distribution, dock scheduling | "cross-docking," "transshipment" |
| [yard-management](yard-management/) | Trailer tracking, dock doors, yard jockey | "yard management," "YMS," "dock scheduling" |

---

### **4. Procurement & Sourcing** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [supplier-selection](supplier-selection/) | Vendor evaluation, RFP scoring, TCO | "supplier selection," "RFP," "vendor evaluation" |
| [procurement-optimization](procurement-optimization/) | Order allocation, lot sizing, multi-sourcing | "procurement optimization," "lot sizing" |
| [supplier-risk-management](supplier-risk-management/) | Risk assessment, FMEA, mitigation | "supplier risk," "risk assessment," "FMEA" |
| [spend-analysis](spend-analysis/) | Spend analytics, Pareto, category management | "spend analysis," "category management" |
| [contract-management](contract-management/) | SLAs, performance tracking, renewals | "contract management," "SLA," "supplier performance" |
| [strategic-sourcing](strategic-sourcing/) | Kraljic matrix, should-cost, e-auctions | "strategic sourcing," "Kraljic," "should-cost" |

---

### **5. Manufacturing & Production** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [production-scheduling](production-scheduling/) | Job shop, finite capacity, Gantt charts | "production scheduling," "job shop," "finite capacity" |
| [lean-manufacturing](lean-manufacturing/) | VSM, 5S, Kanban, waste reduction | "lean manufacturing," "VSM," "Kanban," "5S" |
| [quality-management](quality-management/) | SPC, Six Sigma, control charts, Cpk | "quality management," "SPC," "Six Sigma," "control charts" |
| [maintenance-planning](maintenance-planning/) | Preventive/predictive maintenance, TPM, MTBF | "maintenance planning," "predictive maintenance," "TPM" |
| [process-optimization](process-optimization/) | Bottleneck analysis, simulation, queuing | "process optimization," "bottleneck," "simulation" |
| [assembly-line-balancing](assembly-line-balancing/) | Line balancing, takt time, workstation assignment | "line balancing," "takt time," "assembly line" |

---

### **6. Analytics & Technology** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [supply-chain-analytics](supply-chain-analytics/) | KPIs, dashboards, SCOR metrics, BI | "supply chain analytics," "KPI dashboard," "SCOR" |
| [digital-twin-modeling](digital-twin-modeling/) | Simulation, discrete event, agent-based | "digital twin," "simulation," "discrete event" |
| [ml-supply-chain](ml-supply-chain/) | Machine learning, predictive analytics, XGBoost | "machine learning," "predictive analytics," "ML" |
| [optimization-modeling](optimization-modeling/) | Linear programming, MIP, PuLP, Gurobi | "optimization," "linear programming," "MIP" |
| [supply-chain-automation](supply-chain-automation/) | RPA, workflow automation, API integration | "automation," "RPA," "workflow" |
| [prescriptive-analytics](prescriptive-analytics/) | Decision optimization, recommendations | "prescriptive analytics," "decision support" |

---

### **7. Sustainability & Risk** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [carbon-footprint-tracking](carbon-footprint-tracking/) | Scope 1/2/3 emissions, carbon accounting | "carbon footprint," "emissions," "scope 3" |
| [circular-economy](circular-economy/) | Reverse logistics, remanufacturing, closed-loop | "circular economy," "reverse logistics" |
| [risk-mitigation](risk-mitigation/) | SCRM, business continuity, disruption | "risk mitigation," "SCRM," "business continuity" |
| [compliance-management](compliance-management/) | Regulatory, ESG, audits, certifications | "compliance," "ESG," "regulatory" |
| [sustainable-sourcing](sustainable-sourcing/) | Green procurement, supplier sustainability | "sustainable sourcing," "green procurement" |

---

### **8. Visibility & Collaboration** (4 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [control-tower-design](control-tower-design/) | Real-time visibility, exception management | "control tower," "visibility," "exception management" |
| [supplier-collaboration](supplier-collaboration/) | CPFR, collaborative planning, EDI | "supplier collaboration," "CPFR," "collaborative planning" |
| [demand-supply-matching](demand-supply-matching/) | Allocation, ATP/CTP, supply balancing | "demand-supply matching," "allocation," "ATP" |
| [track-and-trace](track-and-trace/) | Shipment visibility, IoT, blockchain | "track and trace," "shipment visibility," "IoT" |

---

## 🏭 Domain-Specific Verticals

### **9. Retail Supply Chain** (7 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [omnichannel-fulfillment](omnichannel-fulfillment/) | BOPIS, ship-from-store, unified inventory | "omnichannel," "BOPIS," "ship from store" |
| [retail-allocation](retail-allocation/) | Store allocation, size curves, assortment | "retail allocation," "assortment planning" |
| [markdown-optimization](markdown-optimization/) | Price optimization, clearance, promotions | "markdown," "price optimization," "clearance" |
| [planogram-optimization](planogram-optimization/) | Shelf space, category management, adjacency | "planogram," "shelf space," "category management" |
| [retail-replenishment](retail-replenishment/) | Auto-replenishment, DSD, store ordering | "retail replenishment," "auto-replenishment" |
| [ecommerce-fulfillment](ecommerce-fulfillment/) | DC-to-consumer, returns, carrier selection | "ecommerce fulfillment," "returns," "parcel" |
| [seasonal-planning](seasonal-planning/) | Seasonal buy, in-season chase, fashion retail | "seasonal planning," "fashion retail," "seasonal buy" |

---

### **10. Energy Supply Chain** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [energy-logistics](energy-logistics/) | Oil & gas logistics, pipeline, terminals | "energy logistics," "pipeline," "oil and gas" |
| [renewable-energy-planning](renewable-energy-planning/) | Solar/wind supply chains, project planning | "renewable energy," "solar," "wind logistics" |
| [power-grid-optimization](power-grid-optimization/) | Load balancing, optimal power flow, unit commitment | "power grid," "load balancing," "grid optimization" |
| [energy-storage-optimization](energy-storage-optimization/) | Battery systems, arbitrage, peak shaving | "energy storage," "battery," "peak shaving" |
| [drilling-logistics](drilling-logistics/) | Rig scheduling, tubular management, offshore | "drilling logistics," "rig scheduling," "upstream" |
| [fuel-distribution](fuel-distribution/) | Retail fuel, tank truck routing, station inventory | "fuel distribution," "tank truck," "fuel terminal" |

---

### **11. Travel & Hospitality** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [hotel-inventory-management](hotel-inventory-management/) | Revenue management, dynamic pricing, overbooking | "hotel inventory," "revenue management," "dynamic pricing" |
| [tour-operations](tour-operations/) | Tour planning, itinerary optimization, capacity | "tour operations," "tour planning," "itinerary" |
| [airline-cargo-optimization](airline-cargo-optimization/) | Cargo capacity, ULD optimization, yield management | "airline cargo," "ULD," "cargo capacity" |
| [cruise-supply-chain](cruise-supply-chain/) | Ship provisioning, multi-port logistics | "cruise supply chain," "ship provisioning" |
| [hospitality-procurement](hospitality-procurement/) | F&B procurement, hotel purchasing, GPO | "hospitality procurement," "F&B," "hotel purchasing" |

---

### **12. CPG Supply Chain** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [dsd-route-optimization](dsd-route-optimization/) | Direct store delivery, pre-sell, route accounting | "DSD," "direct store delivery," "route accounting" |
| [promotional-planning](promotional-planning/) | Trade promotions, lift forecasting, TPO | "promotional planning," "trade promotions," "TPO" |
| [co-packing-management](co-packing-management/) | Contract manufacturing, co-packer coordination | "co-packing," "contract manufacturing," "co-packer" |
| [cpg-network-design](cpg-network-design/) | Multi-tier distribution, DTC, retail collaboration | "CPG network," "consumer packaged goods" |
| [shelf-life-management](shelf-life-management/) | FEFO, expiry tracking, freshness | "shelf life," "FEFO," "expiration management" |
| [slotting-fees-optimization](slotting-fees-optimization/) | Retail negotiations, SKU rationalization | "slotting fees," "retail negotiations" |

---

### **13. Manufacturing Verticals** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [automotive-supply-chain](automotive-supply-chain/) | JIT/JIS, sequencing, tier management | "automotive supply chain," "JIT," "sequencing" |
| [electronics-supply-chain](electronics-supply-chain/) | Component allocation, NPI, E&O management | "electronics supply chain," "component shortage," "NPI" |
| [pharmaceutical-supply-chain](pharmaceutical-supply-chain/) | Cold chain, serialization, DSCSA, GDP | "pharmaceutical," "cold chain," "serialization," "DSCSA" |
| [food-beverage-supply-chain](food-beverage-supply-chain/) | Perishables, food safety, HACCP, traceability | "food supply chain," "perishables," "HACCP" |
| [aerospace-supply-chain](aerospace-supply-chain/) | Long lead times, AS9100, MRO, AOG | "aerospace supply chain," "AOG," "AS9100," "MRO" |

---

### **14. Healthcare Supply Chain** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [hospital-logistics](hospital-logistics/) | PAR levels, OR scheduling, materials management | "hospital logistics," "PAR levels," "OR scheduling" |
| [medical-device-distribution](medical-device-distribution/) | UDI, consignment, traceability, FDA | "medical device," "UDI," "consignment inventory" |
| [pharmacy-supply-chain](pharmacy-supply-chain/) | DSCSA, controlled substances, 340B | "pharmacy supply chain," "DSCSA," "controlled substances" |
| [clinical-trial-logistics](clinical-trial-logistics/) | IRT/IVRS, drug accountability, GCP | "clinical trial," "IRT," "drug accountability" |
| [value-analysis](value-analysis/) | Product evaluation, formulary, physician preference | "value analysis," "formulary management," "PPI" |

---

## 🔬 Operations Research Problems

### **15. Packing & Loading** (7 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [2d-bin-packing](2d-bin-packing/) | Rectangle packing, guillotine cuts | "2D bin packing," "rectangle packing" |
| [3d-bin-packing](3d-bin-packing/) | Container loading, box stacking, weight distribution | "3D bin packing," "container loading," "box packing" |
| [pallet-loading](pallet-loading/) | Pallet configuration, mixed SKU pallets, stability | "pallet loading," "pallet optimization" |
| [container-loading-optimization](container-loading-optimization/) | 20ft/40ft containers, load plans | "container loading," "FCL," "load plan" |
| [knapsack-problems](knapsack-problems/) | 0/1 knapsack, multi-dimensional, bounded | "knapsack problem," "cargo value optimization" |
| [strip-packing](strip-packing/) | 2D strip packing, shelf algorithms | "strip packing," "cutting stock" |
| [vehicle-loading-optimization](vehicle-loading-optimization/) | Truck loading, fill rate, axle weights | "truck loading," "vehicle loading," "fill rate" |

---

### **16. Routing & Scheduling** (10 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [traveling-salesman-problem](traveling-salesman-problem/) | TSP, exact/heuristic algorithms | "TSP," "traveling salesman," "tour optimization" |
| [vehicle-routing-problem](vehicle-routing-problem/) | Basic VRP, Clarke-Wright, sweep | "VRP," "vehicle routing," "delivery routes" |
| [vrp-time-windows](vrp-time-windows/) | VRPTW, delivery windows | "time windows," "VRPTW," "delivery windows" |
| [capacitated-vrp](capacitated-vrp/) | CVRP, load constraints, multi-trip | "capacitated VRP," "CVRP," "capacity constraints" |
| [multi-depot-vrp](multi-depot-vrp/) | MDVRP, depot assignment | "multi-depot," "MDVRP," "depot assignment" |
| [pickup-delivery-problem](pickup-delivery-problem/) | PDP, paired pickups, precedence | "pickup and delivery," "PDP," "dial-a-ride" |
| [vrp-backhauls](vrp-backhauls/) | Linehaul and backhaul, mixed deliveries | "backhauls," "reverse logistics routing" |
| [split-delivery-vrp](split-delivery-vrp/) | Partial deliveries, load splitting | "split delivery," "partial deliveries" |
| [job-shop-scheduling](job-shop-scheduling/) | JSS, makespan, Gantt charts | "job shop scheduling," "JSS," "makespan" |
| [flow-shop-scheduling](flow-shop-scheduling/) | Permutation flow shop, Johnson's rule | "flow shop," "permutation scheduling" |

---

### **17. Assignment & Allocation** (8 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [warehouse-slotting-optimization](warehouse-slotting-optimization/) | ABC slotting, velocity-based, golden zone | "warehouse slotting," "slot assignment" |
| [dock-door-assignment](dock-door-assignment/) | Inbound/outbound dock scheduling | "dock door assignment," "dock scheduling" |
| [wave-planning-optimization](wave-planning-optimization/) | Order batching, wave release | "wave planning," "wave release" |
| [order-batching-optimization](order-batching-optimization/) | Batch picking, cluster picking | "order batching," "batch picking" |
| [picker-routing-optimization](picker-routing-optimization/) | S-shape, largest gap, optimal routing | "picker routing," "pick path" |
| [workforce-scheduling](workforce-scheduling/) | Shift planning, labor optimization | "workforce scheduling," "shift planning" |
| [task-assignment-problem](task-assignment-problem/) | Hungarian algorithm, LAP | "task assignment," "Hungarian algorithm," "LAP" |
| [load-building-optimization](load-building-optimization/) | LTL consolidation, multi-stop loads | "load building," "shipment consolidation" |

---

### **18. Location & Network** (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [facility-location-problem](facility-location-problem/) | P-median, P-center, UFLP, CFLP | "facility location," "p-median," "p-center" |
| [hub-location-problem](hub-location-problem/) | Hub-and-spoke, hub allocation | "hub location," "hub-and-spoke" |
| [warehouse-location-optimization](warehouse-location-optimization/) | Greenfield analysis, gravity models | "warehouse location," "greenfield analysis" |
| [distribution-center-network](distribution-center-network/) | Multi-echelon, network flow | "DC network," "distribution network" |
| [set-covering-problem](set-covering-problem/) | Minimum set cover, maximal covering | "set covering," "location set covering" |
| [network-flow-optimization](network-flow-optimization/) | Min-cost flow, transportation problem | "network flow," "transportation problem" |

---

### **19. Inventory Models** (7 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [economic-order-quantity](economic-order-quantity/) | EOQ, EPQ, quantity discounts | "EOQ," "economic order quantity" |
| [multi-echelon-inventory](multi-echelon-inventory/) | Installation stock, echelon stock, GSM | "multi-echelon," "echelon stock" |
| [newsvendor-problem](newsvendor-problem/) | Single-period, critical ratio | "newsvendor," "single-period inventory" |
| [lot-sizing-problems](lot-sizing-problems/) | Wagner-Whitin, Silver-Meal, POQ | "lot sizing," "Wagner-Whitin" |
| [dynamic-lot-sizing](dynamic-lot-sizing/) | Time-varying demand, dynamic programming | "dynamic lot sizing," "time-varying demand" |
| [stochastic-inventory-models](stochastic-inventory-models/) | (Q,R), (s,S), service levels | "stochastic inventory," "Q,R policy," "s,S policy" |
| [inventory-routing-problem](inventory-routing-problem/) | IRP, VMI, delivery scheduling | "inventory routing," "IRP," "VMI routing" |

---

### **20. Cutting & Nesting** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [1d-cutting-stock](1d-cutting-stock/) | Linear cutting, column generation | "1D cutting stock," "linear cutting," "trim loss" |
| [2d-cutting-stock](2d-cutting-stock/) | Sheet cutting, guillotine/non-guillotine | "2D cutting stock," "sheet cutting" |
| [nesting-optimization](nesting-optimization/) | Irregular shapes, CNC cutting | "nesting," "irregular shapes," "polygon packing" |
| [trim-loss-minimization](trim-loss-minimization/) | Paper/steel/textile cutting, waste reduction | "trim loss," "waste reduction," "material utilization" |
| [guillotine-cutting](guillotine-cutting/) | Staged cutting, orthogonal cuts | "guillotine cutting," "staged cutting" |

---

## 🚀 Advanced Optimization & AI

### **21. Advanced Optimization** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [metaheuristic-optimization](metaheuristic-optimization/) | Genetic algorithms, simulated annealing, tabu search | "genetic algorithm," "simulated annealing," "metaheuristic" |
| [column-generation](column-generation/) | Branch-and-price, Dantzig-Wolfe | "column generation," "branch and price" |
| [constraint-programming](constraint-programming/) | CP-SAT, domain reduction, propagation | "constraint programming," "CP-SAT" |
| [stochastic-optimization](stochastic-optimization/) | Two-stage, chance-constrained, robust | "stochastic optimization," "robust optimization" |
| [multi-objective-optimization](multi-objective-optimization/) | Pareto frontier, weighted objectives, NSGA-II | "multi-objective," "Pareto," "NSGA-II" |

---

### **22. AI & Machine Learning** (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [reinforcement-learning-supply-chain](reinforcement-learning-supply-chain/) | Q-learning, DQN, inventory control | "reinforcement learning," "Q-learning," "DQN" |
| [neural-networks-forecasting](neural-networks-forecasting/) | LSTM, transformers, attention mechanisms | "LSTM," "neural network forecasting," "transformers" |
| [optimization-ml-hybrid](optimization-ml-hybrid/) | Learning to optimize, neural combinatorial | "hybrid optimization," "learning to optimize" |
| [computer-vision-warehouse](computer-vision-warehouse/) | Object detection, OCR, quality inspection | "computer vision," "object detection," "YOLO" |
| [nlp-supply-chain](nlp-supply-chain/) | Document processing, chatbots, demand signals | "NLP," "natural language," "document processing" |

---

## 🔧 Installation Options

### Option 1: Claude Code Plugin (Recommended)

Install as a complete plugin for Claude Code:

```bash
# Clone the repository
git clone https://github.com/kishorkukreja/awesome-supply-chain.git
cd awesome-supply-chain

# Install all 132 skills
cp -r skills/* ~/.claude/skills/
```

### Option 2: Select Specific Skills

Install only the skills you need:

```bash
cd awesome-supply-chain/skills

# Example: Install forecasting and routing skills
cp -r demand-forecasting ~/.claude/skills/
cp -r vehicle-routing-problem ~/.claude/skills/
cp -r inventory-optimization ~/.claude/skills/
cp -r warehouse-slotting-optimization ~/.claude/skills/
```

### Option 3: Symlink for Auto-Updates

Create a symbolic link to get automatic updates:

```bash
# Link entire skills directory
ln -s /path/to/awesome-supply-chain/skills ~/.claude/skills/supply-chain

# Or link individual skills
ln -s /path/to/awesome-supply-chain/skills/demand-forecasting ~/.claude/skills/demand-forecasting
```

### Option 4: Git Submodule

Add to your project as a submodule:

```bash
cd your-supply-chain-project
git submodule add https://github.com/kishorkukreja/awesome-supply-chain.git
ln -s awesome-supply-chain/skills/* ~/.claude/skills/
```

---

## 💻 Usage

Once installed, your AI coding assistant will automatically detect when you're working on supply chain problems and apply the relevant skill frameworks.

### Automatic Skill Activation

Skills trigger based on keywords in your conversation:

**Example prompts:**

```bash
"Help me optimize my warehouse slotting using ABC analysis"
→ Automatically uses warehouse-slotting-optimization skill

"Build a demand forecasting model with seasonality"
→ Automatically uses demand-forecasting skill

"Solve this vehicle routing problem with time windows"
→ Automatically uses vrp-time-windows skill

"Design a distribution network with 3 potential DC locations"
→ Uses network-design and facility-location-problem skills

"Implement a genetic algorithm for production scheduling"
→ Uses production-scheduling and metaheuristic-optimization skills
```

### Direct Skill Invocation

You can also explicitly invoke skills:

```bash
"Use the knapsack-problems skill to maximize cargo value"
"Apply lean-manufacturing principles to reduce waste"
"Run the newsvendor-problem analysis for seasonal products"
"Use economic-order-quantity skill to calculate optimal order quantities"
```

### Compatible AI Coding Assistants

This plugin works with:
- ✅ **Claude Code** (Anthropic's official CLI)
- ✅ **Cursor** (AI-powered IDE)
- ✅ **Aider** (AI pair programming in terminal)
- ✅ **Continue** (VS Code / JetBrains extension)
- ✅ **GitHub Copilot** (with workspace instructions)
- ✅ **Cody** (Sourcegraph's AI assistant)
- ✅ **Any coding assistant supporting custom skills/instructions**

---

## 🐍 Python Libraries Used

Skills leverage these powerful Python libraries:

**Optimization:**
- `pulp` - Linear programming
- `pyomo` - Optimization modeling
- `ortools` (Google OR-Tools) - Constraint programming and routing
- `scipy.optimize` - Scientific optimization
- `cvxpy` - Convex optimization

**Data Science & ML:**
- `pandas`, `numpy` - Data manipulation
- `scikit-learn` - Machine learning
- `xgboost`, `lightgbm` - Gradient boosting
- `tensorflow`, `pytorch` - Deep learning
- `statsmodels` - Statistical modeling
- `prophet` - Time series forecasting

**Simulation & Visualization:**
- `simpy` - Discrete event simulation
- `networkx` - Network analysis
- `matplotlib`, `seaborn`, `plotly` - Visualization

**Specialized:**
- `shapely` - Geometric operations
- `opencv` - Computer vision
- `transformers` - NLP and neural networks

---

## 🏢 Commercial Software Referenced

Skills also reference industry-standard commercial platforms:

- **ERP:** SAP, Oracle, Microsoft Dynamics
- **Supply Chain Planning:** Blue Yonder, Kinaxis, o9 Solutions, Anaplan
- **Optimization:** Gurobi, CPLEX, FICO Xpress
- **Simulation:** AnyLogic, Arena, FlexSim, Simio
- **WMS:** Manhattan, Blue Yonder, Oracle WMS
- **TMS:** Blue Yonder, MercuryGate, Oracle TMS

---

## 🎯 Who Should Use This?

- **Supply Chain Managers** - Optimize operations with AI-powered analysis
- **Operations Research Analysts** - Implement OR algorithms quickly
- **Data Scientists** - Apply ML to supply chain problems
- **Logistics Engineers** - Solve routing and network design problems
- **Inventory Planners** - Optimize stock levels and replenishment
- **Manufacturing Engineers** - Improve production scheduling
- **Procurement Professionals** - Optimize sourcing and supplier selection
- **Students & Researchers** - Learn supply chain optimization techniques

---

## 📖 Skill Structure

Each SKILL.md file follows a consistent structure:

```markdown
---
name: skill-name
description: When to use this skill and trigger keywords
---

# Skill Name

Expert role definition

## Initial Assessment
Questions to understand the problem context

## Frameworks & Methodologies
Industry best practices and approaches

## Algorithms & Models
Mathematical formulations and solution methods

## Python Code Examples
Working implementations

## Tools & Libraries
Recommended software and packages

## Common Challenges & Solutions
Real-world problem solving

## Output Format
Templates for deliverables

## Related Skills
Cross-references to other skills
```

---

## 🤝 Contributing

Contributions welcome! Ways to contribute:

1. **Improve existing skills** - Add algorithms, examples, or clarify explanations
2. **Add new skills** - Suggest additional supply chain problem areas
3. **Fix errors** - Correct typos, bugs, or outdated information
4. **Share examples** - Add real-world case studies or datasets
5. **Optimize code** - Improve performance or add features

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Make your changes
4. Test the code examples
5. Submit a pull request with clear description

---

## 📊 Skill Statistics

- **Total Skills:** 132
- **Total Lines of Code:** 150,000+
- **Python Examples:** 500+
- **Optimization Models:** 100+
- **Algorithms Implemented:** 200+

**Coverage:**
- ✅ All major supply chain functions
- ✅ 6+ industry verticals
- ✅ 40+ classic OR problems
- ✅ Modern ML/AI techniques
- ✅ Strategic to operational decisions

---

## 📚 Learning Path

**Beginner Supply Chain:**
1. demand-forecasting
2. inventory-optimization
3. supply-chain-analytics

**Intermediate Operations Research:**
1. vehicle-routing-problem
2. facility-location-problem
3. economic-order-quantity

**Advanced Optimization:**
1. metaheuristic-optimization
2. column-generation
3. multi-objective-optimization

**ML & AI Applications:**
1. ml-supply-chain
2. reinforcement-learning-supply-chain
3. neural-networks-forecasting

---

## 🌟 Highlights

**Most Comprehensive Skills:**
- `demand-forecasting` - Complete forecasting framework with 10+ methods
- `network-design` - Full network optimization with MIP models
- `vehicle-routing-problem` - Multiple VRP variants and algorithms
- `warehouse-slotting-optimization` - Advanced slotting with QAP

**Best for Beginners:**
- `economic-order-quantity` - Clear EOQ derivations
- `traveling-salesman-problem` - Classic TSP algorithms
- `supply-chain-analytics` - KPI dashboards and metrics

**Most Advanced:**
- `column-generation` - Branch-and-price implementation
- `reinforcement-learning-supply-chain` - DQN for inventory
- `optimization-ml-hybrid` - Learning to optimize

---

## 📄 License

MIT License - Use these skills however you want for commercial or personal projects.

---

## 🙏 Acknowledgments

Built for the supply chain community by leveraging:
- Operations research literature and textbooks
- Industry best practices
- Open-source optimization libraries
- Real-world supply chain experience

---

## 📞 Support

- **Issues:** Report problems or suggest improvements via GitHub Issues
- **Discussions:** Share use cases and ask questions in Discussions
- **Documentation:** Each skill has detailed documentation and examples

---

**Last Updated:** January 2026

**Repository:** [awesome-supply-chain](https://github.com/yourusername/awesome-supply-chain)
