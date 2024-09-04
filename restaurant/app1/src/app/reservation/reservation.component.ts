// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-reservation',
//   templateUrl: './reservation.component.html',
//   styleUrl: './reservation.component.css'
// })
// export class ReservationComponent {

// }
import { Component } from '@angular/core';
import { ReservationService } from '../reservation.service';

@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.css']
})
export class ReservationComponent {

  reservationData = {
    name: '',
    email: '',
    persons: 1,
    date: '',
    time: ''
  };

  constructor(private reservationService: ReservationService) { }

  submitReservation() {
    this.reservationService.makeReservation(this.reservationData).subscribe(response => {
      if (response.status === 'success') {
        alert('Reservation made successfully!');
      } else {
        alert('Failed to make reservation.');
      }
    });
  }
}
