/** @odoo-module */

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";
import { onWillStart, useState, onWillUpdateProps, Component } from "@odoo/owl";

export class SmartMarginCard extends Component {
    static template = "smart_margin.SmartMarginCard";
    static props = {
        ...standardWidgetProps,
    };

    setup() {
        super.setup();

        this.action = useService("action");
        this.orm = useService("orm");
        this.state = useState({
            revenue: 0,
            cogs: 0,
            net: 0,
        });
       onWillStart(async () => await this.fetchMargin());


    }
    async fetchMargin()
    {
    const result = await this.orm.call("sale.order","get_smart_margin",[this.props.record.resId]);
    this.state.revenue=result.revenue;
    this.state.cogs=result.cogs;
    this.state.net=result.net;

    }

    openBreakdownPopup()
    {
    this.action.doAction({
            type: "ir.actions.client",
            tag:"smart_margin.popup",
            target:"new",
            params: {orderId:this.props.record.resId}

        });

    }

}

export const smartMargin = {
    component: SmartMarginCard,
};
registry.category("view_widgets").add("sale_smart_margin", smartMargin);
