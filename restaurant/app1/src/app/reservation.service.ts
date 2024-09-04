// import { Injectable } from '@angular/core';

// @Injectable({
//   providedIn: 'root'
// })
// export class ReservationService {

//   constructor() { }
// }
//hihiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {

  private apiUrl = 'http://localhost:8000/api/make_reservation/';

  constructor(private http: HttpClient) { }

  makeReservation(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
