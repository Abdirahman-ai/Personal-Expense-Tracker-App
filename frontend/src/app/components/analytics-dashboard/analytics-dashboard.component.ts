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

  @Input() expenses: any[] = [];

  categoryBarChartType: ChartType = 'bar';
  paymentPieChartType: ChartType = 'pie';
  monthlyLineChartType: ChartType = 'line';
  yearlyBarChartType: ChartType = 'bar';

  categoryBarChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [{ label: 'Spending by Category', data: [] }]
  };

  paymentPieChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [{ label: 'Spending by Payment Method', data: [] }]
  };

  monthlyLineChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [{ label: 'Monthly Spending Trend', data: [] }]
  };

  yearlyBarChartData: ChartConfiguration['data'] = {
    labels: [],
    datasets: [{ label: 'Yearly Spending Summary', data: [] }]
  };

  categoryBarChartOptions: ChartConfiguration['options'] = {
    responsive: true,
     maintainAspectRatio: false,
    plugins: { legend: { display: true } }
  };

  paymentPieChartOptions: ChartConfiguration['options'] = {
    responsive: true,
     maintainAspectRatio: false,
    plugins: { legend: { display: true, position: 'bottom' } }
  };

  monthlyLineChartOptions: ChartConfiguration['options'] = {
    responsive: true,
     maintainAspectRatio: false,
    plugins: { legend: { display: true } }
  };

  yearlyBarChartOptions: ChartConfiguration['options'] = {
    responsive: true,
     maintainAspectRatio: false,
    plugins: { legend: { display: true } }
  };

  ngOnChanges(): void {
    this.updateCharts();
  }

  updateCharts(): void {
    const categoryTotals: { [key: string]: number } = {};
    const paymentTotals: { [key: string]: number } = {};
    const monthlyTotals: { [key: string]: number } = {};
    const yearlyTotals: { [key: string]: number } = {};

    this.expenses.forEach(expense => {
      categoryTotals[expense.category] =
        (categoryTotals[expense.category] || 0) + Number(expense.amount);

      paymentTotals[expense.payment_method] =
        (paymentTotals[expense.payment_method] || 0) + Number(expense.amount);

      const month = expense.date.substring(0, 7);
      monthlyTotals[month] =
        (monthlyTotals[month] || 0) + Number(expense.amount);

      const year = expense.date.substring(0, 4);
      yearlyTotals[year] =
        (yearlyTotals[year] || 0) + Number(expense.amount);
    });

    this.categoryBarChartData = {
      labels: Object.keys(categoryTotals),
      datasets: [{ label: 'Spending by Category', data: Object.values(categoryTotals) }]
    };

    this.paymentPieChartData = {
      labels: Object.keys(paymentTotals),
      datasets: [{ label: 'Spending by Payment Method', data: Object.values(paymentTotals) }]
    };

    const sortedMonths = Object.keys(monthlyTotals).sort();

    this.monthlyLineChartData = {
      labels: sortedMonths,
      datasets: [
        {
          label: 'Monthly Spending Trend',
          data: sortedMonths.map(month => monthlyTotals[month])
        }
      ]
    };

    const sortedYears = Object.keys(yearlyTotals).sort();

    this.yearlyBarChartData = {
      labels: sortedYears,
      datasets: [
        {
          label: 'Yearly Spending Summary',
          data: sortedYears.map(year => yearlyTotals[year])
        }
      ]
    };
  }
}
