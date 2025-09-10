/** @odoo-module */

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";
import { onWillStart, useState, onWillUpdateProps, Component } from "@odoo/owl";

export class MarginBreakdownPopup extends Component {
    static template = "smart_margin.MarginBreakdownPopup";


    setup() {
        super.setup();

        this.action = useService("action");
        this.orm = useService("orm");
        this.state = useState({
            lines:[],
            expanded:{}
        });
       onWillStart(async () => {
       //fetch lines from so
           const result = await this.orm.call("sale.order","get_margin_breakdown",[this.props.action.params.orderId]);
           this.state.lines=result;


       });


    }

    get totalRow()
    {
     const sum = ( field) => this.state.lines.reduce(  (a,l)=> a+l[field],0 );
     return {product:"Total",
            qty:sum("qty"),
            price_unit:"",
            landed_cost:sum("landed_cost"),
            overhead_cost : sum("overhead_cost"),
            line_margin : sum("line_margin")
     }

    }

    toggleRow(comp,product)
    {
    comp.state.expanded[product]=!comp.state.expanded[product];
    }




}


registry.category("actions").add("smart_margin.popup", MarginBreakdownPopup);
