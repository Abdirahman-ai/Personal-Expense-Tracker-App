import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Expense } from '../../models/expense';
import { ExpenseService } from '../../services/expense.service';

@Component({
  selector: 'app-expense-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './expense-list.component.html',
  styleUrl: './expense-list.component.css'
})
export class ExpenseListComponent implements OnInit {

  expenses: Expense[] = [];

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
    return this.expenses.reduce((total, expense) => total + Number(expense.amount), 0);
  }

  getAverageExpense(): number {
    if (this.expenses.length === 0) return 0;
    return this.getTotalSpending() / this.expenses.length;
  }
}
