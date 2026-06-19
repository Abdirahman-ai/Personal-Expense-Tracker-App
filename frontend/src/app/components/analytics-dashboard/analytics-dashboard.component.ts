import { CommonModule } from '@angular/common';
import { BaseChartDirective } from 'ng2-charts';
import { ChartConfiguration, ChartType } from 'chart.js';
import { Component, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [CommonModule, BaseChartDirective],
  templateUrl: './analytics-dashboard.component.html',
  styleUrl: './analytics-dashboard.component.css'
})
export class AnalyticsDashboardComponent implements OnChanges {

  categoryBarChartType: ChartType = 'bar';
  paymentPieChartType: ChartType = 'pie';
  @Input() expenses: any[] = [];

  categoryBarChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [
      {
        label: 'Spending by Category',
        data: []
      }
    ]
  };

  categoryBarChartOptions: ChartConfiguration['options'] = {
    responsive: true,
    plugins: {
      legend: {
        display: true
      }
    }
  };

  paymentPieChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [
      {
        label: 'Spending by Payment Method',
        data: []
      }
    ]
  };

 paymentPieChartOptions: ChartConfiguration['options'] = {
   responsive: true,
   plugins: {
     legend: {
       display: true,
       position: 'bottom'
     }
   }
 };
  ngOnChanges(): void {
    this.updateCharts();
  }

  updateCharts(): void {
    const categoryTotals: { [key: string]: number } = {};
    const paymentTotals: { [key: string]: number } = {};

    this.expenses.forEach(expense => {
      categoryTotals[expense.category] =
        (categoryTotals[expense.category] || 0) + Number(expense.amount);

      paymentTotals[expense.payment_method] =
        (paymentTotals[expense.payment_method] || 0) + Number(expense.amount);
    });

    this.categoryBarChartData = {
      labels: Object.keys(categoryTotals),
      datasets: [
        {
          label: 'Spending by Category',
          data: Object.values(categoryTotals)
        }
      ]
    };

    this.paymentPieChartData = {
      labels: Object.keys(paymentTotals),
      datasets: [
        {
          label: 'Spending by Payment Method',
          data: Object.values(paymentTotals)
        }
      ]
    };
  }
}
