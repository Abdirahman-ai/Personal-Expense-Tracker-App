import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { BaseChartDirective } from 'ng2-charts';
import { ChartConfiguration, ChartType } from 'chart.js';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [CommonModule, BaseChartDirective],
  templateUrl: './analytics-dashboard.component.html',
  styleUrl: './analytics-dashboard.component.css'
})
export class AnalyticsDashboardComponent implements OnInit {

  categoryBarChartType: ChartType = 'bar';
  paymentPieChartType: ChartType = 'pie';

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

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadCategorySummary();
    this.loadPaymentSummary();
  }

  loadCategorySummary(): void {
    this.http.get<any[]>('http://127.0.0.1:8000/analytics/category-summary')
      .subscribe({
        next: (data) => {
          this.categoryBarChartData = {
            labels: data.map(item => item.category),
            datasets: [
              {
                label: 'Spending by Category',
                data: data.map(item => item.total)
              }
            ]
          };
        },
        error: (error) => {
          console.error('Error loading category summary', error);
        }
      });
  }

  loadPaymentSummary(): void {
    this.http.get<any[]>('http://127.0.0.1:8000/analytics/payment-summary')
      .subscribe({
        next: (data) => {
          this.paymentPieChartData = {
            labels: data.map(item => item.payment_method),
            datasets: [
              {
                label: 'Spending by Payment Method',
                data: data.map(item => item.total)
              }
            ]
          };
        },
        error: (error) => {
          console.error('Error loading payment summary', error);
        }
      });
  }
}
