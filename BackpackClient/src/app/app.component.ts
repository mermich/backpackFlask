import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styles: []
})
export class AppComponent implements OnInit {
  title = 'BackpackClient';

  constructor(private httpClient: HttpClient, private router: Router) { }

  ngOnInit(): void {
    this.router.navigate(['/InventoryItemsList']);
  }

}
