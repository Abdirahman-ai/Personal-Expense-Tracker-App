import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ExpenseListComponent } from './components/expense-list/expense-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ExpenseListComponent],
  template: `<app-expense-list></app-expense-list>`
})
export class AppComponent {
  title = 'frontend';
}
