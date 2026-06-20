import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Expense } from '../../models/expense';
import { ExpenseService } from '../../services/expense.service';

import { AnalyticsDashboardComponent } from '../analytics-dashboard/analytics-dashboard.component';

@Component({
  selector: 'app-expense-list',
  standalone: true,
  imports: [CommonModule, FormsModule, AnalyticsDashboardComponent],
  templateUrl: './expense-list.component.html',
  styleUrl: './expense-list.component.css'
})
export class ExpenseListComponent implements OnInit {

  isEditing: boolean = false;
  editingExpenseId: number | undefined = undefined;

  expenses: Expense[] = [];
  searchTitle: string = '';
  startDate: string = '';
  endDate: string = '';
  sortOption: string = 'date-desc';
  viewMode: string = 'all';

  newExpense: Expense = {
    title: '',
    category: '',
    amount: 0,
    date: '',
    payment_method: ''
  };

  constructor(private expenseService: ExpenseService) {}

  ngOnInit(): void {
    this.loadExpenses();
  }

  loadExpenses(): void {
    this.expenseService.getAllExpenses().subscribe({
      next: (data) => this.expenses = data,
      error: (error) => console.error('Error loading expenses', error)
    });
  }

  addExpense(): void {
    this.expenseService.createExpense(this.newExpense).subscribe({
      next: () => {
        this.loadExpenses();
        this.newExpense = {
          title: '',
          category: '',
          amount: 0,
          date: '',
          payment_method: ''
        };
      },
      error: (error) => console.error('Error adding expense', error)
    });
  }

  deleteExpense(id: number | undefined): void {
    if (!id) return;

    this.expenseService.deleteExpense(id).subscribe({
      next: () => this.loadExpenses(),
      error: (error) => console.error('Error deleting expense', error)
    });
  }

  getTotalSpending(): number {
    return this.getFilteredExpenses()
      .reduce((total, expense) => total + Number(expense.amount), 0);
  }

  getAverageExpense(): number {
    const filteredExpenses = this.getFilteredExpenses();

    if (filteredExpenses.length === 0) return 0;

    return this.getTotalSpending() / filteredExpenses.length;
  }

  editExpense(expense: Expense): void {
    this.isEditing = true;
    this.editingExpenseId = expense.id;

    this.newExpense = {
      id: expense.id,
      title: expense.title,
      category: expense.category,
      amount: expense.amount,
      date: expense.date,
      payment_method: expense.payment_method
    };
  }

  cancelEdit(): void {
    this.isEditing = false;
    this.editingExpenseId = undefined;

    this.newExpense = {
      title: '',
      category: '',
      amount: 0,
      date: '',
      payment_method: ''
    };
  }

  saveExpense(): void {
    if (this.isEditing && this.editingExpenseId) {
      this.expenseService.updateExpense(this.editingExpenseId, this.newExpense).subscribe({
        next: () => {
          this.loadExpenses();
          this.cancelEdit();
        },
        error: (error) => console.error('Error updating expense', error)
      });
    } else {
      this.addExpense();
    }
  }

  getFilteredExpenses(): Expense[] {

    let filteredExpenses = [...this.expenses];

    if (this.searchTitle.trim()) {
      filteredExpenses = filteredExpenses.filter(expense =>
        expense.title.toLowerCase().includes(
          this.searchTitle.toLowerCase()
        )
      );
    }

    if (this.startDate) {
      filteredExpenses = filteredExpenses.filter(expense =>
        expense.date >= this.startDate
      );
    }

    if (this.endDate) {
      filteredExpenses = filteredExpenses.filter(expense =>
        expense.date <= this.endDate
      );
    }

    switch (this.sortOption) {

      case 'date-desc':
        filteredExpenses.sort((a, b) =>
          b.date.localeCompare(a.date)
        );
        break;

      case 'date-asc':
        filteredExpenses.sort((a, b) =>
          a.date.localeCompare(b.date)
        );
        break;

      case 'amount-desc':
        filteredExpenses.sort((a, b) =>
          b.amount - a.amount
        );
        break;

      case 'amount-asc':
        filteredExpenses.sort((a, b) =>
          a.amount - b.amount
        );
        break;

      case 'title-asc':
        filteredExpenses.sort((a, b) =>
          a.title.localeCompare(b.title)
        );
        break;

      case 'title-desc':
        filteredExpenses.sort((a, b) =>
          b.title.localeCompare(a.title)
        );
        break;
    }

    return filteredExpenses;
  }

  clearFilters(): void {
    this.searchTitle = '';
    this.startDate = '';
    this.endDate = '';
  }

  getMostExpensiveExpense(): number {
    const filteredExpenses = this.getFilteredExpenses();

    if (filteredExpenses.length === 0) {
      return 0;
    }

    return Math.max(...filteredExpenses.map(expense => Number(expense.amount)));
  }

  getTopCategory(): string {
    const filteredExpenses = this.getFilteredExpenses();

    if (filteredExpenses.length === 0) {
      return 'N/A';
    }

    const counts: { [key: string]: number } = {};

    filteredExpenses.forEach(expense => {
      counts[expense.category] = (counts[expense.category] || 0) + 1;
    });

    return Object.keys(counts).reduce((a, b) =>
      counts[a] > counts[b] ? a : b
    );
  }

  getMostUsedPaymentMethod(): string {
    const filteredExpenses = this.getFilteredExpenses();

    if (filteredExpenses.length === 0) {
      return 'N/A';
    }

    const counts: { [key: string]: number } = {};

    filteredExpenses.forEach(expense => {
      counts[expense.payment_method] =
        (counts[expense.payment_method] || 0) + 1;
    });

    return Object.keys(counts).reduce((a, b) =>
      counts[a] > counts[b] ? a : b
    );
  }

  getMonthlySummary(): { period: string; total: number; count: number }[] {
    const monthlyTotals: { [key: string]: { total: number; count: number } } = {};

    this.getFilteredExpenses().forEach(expense => {
      const month = expense.date.substring(0, 7);

      if (!monthlyTotals[month]) {
        monthlyTotals[month] = { total: 0, count: 0 };
      }

      monthlyTotals[month].total += Number(expense.amount);
      monthlyTotals[month].count++;
    });

    return Object.keys(monthlyTotals).map(month => ({
      period: month,
      total: monthlyTotals[month].total,
      count: monthlyTotals[month].count
    }));
  }

  getYearlySummary(): { period: string; total: number; count: number }[] {
    const yearlyTotals: { [key: string]: { total: number; count: number } } = {};

    this.getFilteredExpenses().forEach(expense => {
      const year = expense.date.substring(0, 4);

      if (!yearlyTotals[year]) {
        yearlyTotals[year] = { total: 0, count: 0 };
      }

      yearlyTotals[year].total += Number(expense.amount);
      yearlyTotals[year].count++;
    });

    return Object.keys(yearlyTotals).map(year => ({
      period: year,
      total: yearlyTotals[year].total,
      count: yearlyTotals[year].count
    }));
  }
}
