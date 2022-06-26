'use strict';

// prettier-ignore
//this above line is used to say prettier to ignore the next line
const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

const form = document.querySelector('.form');
const containerWorkouts = document.querySelector('.workouts');
const inputType = document.querySelector('.form__input--type');
const inputDistance = document.querySelector('.form__input--distance');
const inputDuration = document.querySelector('.form__input--duration');
const inputCadence = document.querySelector('.form__input--cadence');
const inputElevation = document.querySelector('.form__input--elevation');
let coordinates;
let EditorData;
// let map;
//navigator(Getting The Location)
// .getBoundingClientRect().x to get the coordinates which we know

//Browser API
let map;
let Icon = L.icon({
  iconUrl: 'outline_my_location_black_24dp.png',
  iconSize: [35, 50],
  iconAnchor: [22, 94],
  popupAnchor: [-3, -76],
  shadowUrl: 'outline_my_location_black_24dp.png',
  shadowSize: [0, 0],
  shadowAnchor: [0, 0],
});
//this is to check whether geolocation supports the browser or not
// navigator.geolocation.getCurrentPosition(
//   function (position) {
//     console.log(position);
//     console.log(position.coords.latitude);
//     console.log(position.coords.longitude);
//     let { latitude, longitude } = position.coords;
//     // console.log('Link For Google Map:');
//     // console.log(`https://www.google.com/maps/@${latitude},${longitude}`);
//     let coords = [latitude, longitude];
//     map = L.map('map').setView(coords, 17);

//     //L.map('x') Here x refers to the div in which we want to display the Map
//     //.setView(coords, y); y refers to how much we want to zoom.
//     //   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     //     attribution:
//     //       '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//     //   }).addTo(map);
//     //   L.tileLayer(
//     //     'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
//     //     {
//     //       attribution:
//     //         'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
//     //     }
//     //   ).addTo(map);
//     L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
//       maxZoom: 19,
//       attribution: '&copy;',
//     }).addTo(map);

//     L.marker(coords)
//       .addTo(map)
//       .bindPopup(
//         L.popup({
//           maxWidth: 250,
//           minWidth: 100,
//           autoClose: false,
//           closeOnClick: false,
//           className: 'running-popup',
//         })
//       )
//       .setPopupContent('Your Current Location')
//       .openPopup();

//     //Here Though 'L' is stored as a global variable in other script but we can use it here also as a global variable as of declared in this script
//     console.log(Fullname);
//     map.on('click', function (MapEvent) {
//       let { lat: latitude, lng: longitude } = MapEvent.latlng;
//       coordinates = [latitude, longitude];
//       form.classList.remove('hidden');
//       inputDistance.focus(); //used to make it blink
//     });

//     //Though Fullname is not declared here but it can be used as it is declared in other js file and we have its link in the html.
//     // map.on('click', function (MapEvent) {
//     //   //It is same like Event Listener but this is not stored in Javascript instead it belongs to a library.
//     //   console.log(MapEvent);
//     //   let { lat: latitude, lng: longitude } = MapEvent.latlng;
//     //   let coords = [latitude, longitude];
//     //   // L.marker(coords, { opacity: 0.7, draggable: true, riseOnHover: true })
//     //   //   .addTo(map)
//     //   //   .bindPopup(
//     //   //     // `Your Marked Location Latitude : ${Math.round(
//     //   //     //   latitude
//     //   //     // )} , Longitude : ${Math.round(longitude)}`
//     //   //     L.popup({
//     //   //       maxWidth: 250,
//     //   //       minWidth: 100,
//     //   //       autoClose: false,
//     //   //       closeOnClick: false,
//     //   //       className: 'running-popup',
//     //   //     })
//     //   //   )
//     //   //   .setPopupContent(
//     //   //     `Your Marked Location Latitude : ${Math.round(
//     //   //       latitude
//     //   //     )} , Longitude : ${Math.round(longitude)}`
//     //   //   )
//     //   //   .openPopup();

//     // });
//   },
//   function () {
//     alert(
//       'Could Not Find Your Location !! Please Allow us to have your location'
//     );
//   }
// );
//Here we need to provide Two functions that is something has to happen when we do a action and the first one is responsible for when we allow the llocation and what has to happen and second one is responsible for what has to happen when location is Blocked and it is like the event Handlers which is quite logical.

// console.log(map);
for (let i = 1; i < 6; i++) {
  console.log('*'.repeat(i));
}

//In a Form here we dont need a button but it can be submitted using the enter key and thus this event can be captured using 'submit' event

//we can also get access to a event when we select something out of the select options

class Workout {
  click = 0;
  Date = new Date();

  constructor(Coordinates, distance, Duration) {
    this['Marked Coordinates'] = Coordinates;
    this['Distance Covered'] = distance;
    this.Duration = Duration;

    this.RandomNum = function (num1, num2) {
      return Math.trunc(Math.random() * (num2 - num1)) + num1;
    };
    this.UID =
      this.Duration +
      this.RandomNum(20, 225) +
      this.RandomNum(122, 10002) +
      this.RandomNum(this.RandomNum(200, 3900), this.RandomNum(120, 12002)) +
      (this.Date + '')
        .split(' ')
        .filter(mov => mov !== ' ')
        .join('')
        .slice(7, 10) +
      this.RandomNum(
        this.RandomNum(
          this.RandomNum(23300, 10003),
          this.RandomNum(23303, 1888202)
        ),
        this.RandomNum(
          this.RandomNum(23300, 793003),
          this.RandomNum(203030, 1000333)
        )
      );
  }
  _click() {
    this.click++;
  }
}

class Running extends Workout {
  #today = new Intl.DateTimeFormat('en-US', {
    month: 'long',
    day: 'numeric',
  }).format(new Date());
  constructor(Coordinates, distance, Duration, Cadence) {
    super(Coordinates, distance, Duration);
    this.type = 'running';
    this.Cadence = Cadence;
    this.CalcPace();
    this.Description = this._setDescription();
  }
  Day() {
    return this.#today;
  }
  CalcPace() {
    //min/km
    this.Pace = this.Duration / this['Distance Covered'];
    return this.Pace;
  }
  _setDescription() {
    return `Running on ${this.#today}`;
  }
}
class Cycling extends Workout {
  #today = new Intl.DateTimeFormat('en-US', {
    month: 'long',
    day: 'numeric',
  }).format(new Date());
  constructor(Coordinates, distance, Duration, ElevationGain) {
    super(Coordinates, distance, Duration);
    this.type = 'cycling';
    this.ElevationGain = ElevationGain;
    this.CalcSpeed();
    this.Description = this._setDescription();
  }
  Day() {
    return this.#today;
  }

  CalcSpeed() {
    //km/h
    this.Speed = this['Distance Covered'] / (this.Duration / 60);
    return this.Speed;
  }
  _setDescription() {
    return `Cycling on ${this.#today}`;
  }
}

class App {
  #currentLocation;
  #Usercoordinates;
  #map;
  #DataArr = [];
  #ClickedCoordinates = [];
  constructor() {
    this._getposition();
    form.addEventListener('submit', this._newWorkout.bind(this));
    containerWorkouts.addEventListener('click', this._MoveToPopUp.bind(this));
    document
      .querySelector('.logo')
      .addEventListener('click', this._SwitchToCurrent.bind(this));
    this._initialLoad();
  }

  _SwitchToCurrent() {
    this.#map.setView(this.#currentLocation, 17, {
      animate: true,
      pan: { duration: 1 },
    });
  }

  _getposition() {
    navigator.geolocation.getCurrentPosition(
      this._loadMap.bind(this),
      function () {
        alert('We cannot get Your Location');
      }
    );
  }
  _setCoords(position) {
    let { latitude, longitude } = position.coords;
    this.#Usercoordinates = [latitude, longitude];
  }
  _loadMap(position) {
    let { latitude, longitude } = position.coords;
    let coords = [latitude, longitude];
    this.#currentLocation = coords;
    map = L.map('map').setView(coords, 17);
    this.#map = map;
    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy;',
    }).addTo(this.#map);

    L.marker(coords)
      .addTo(this.#map)
      .bindPopup(
        L.popup({
          maxWidth: 250,
          minWidth: 100,
          autoClose: false,
          closeOnClick: false,
          className: 'running-popup',
        })
      )
      .setPopupContent('Your Current Location')
      .openPopup();
    this.#Usercoordinates = { Latitude: latitude, Longitude: longitude };
    console.log(this);
    this._showForm();
    this._toggleElevationField();
  }
  _returnMap() {
    return this.#map;
  }

  _showForm() {
    this.#map.on('click', function (MapEvent) {
      let { lat: latitude, lng: longitude } = MapEvent.latlng;
      coordinates = [latitude, longitude];
      Application.#ClickedCoordinates.push(coordinates);
      form.classList.remove('hidden');
      inputDistance.focus(); //used to make it blink
    });
  }
  _toggleElevationField() {
    inputType.addEventListener('change', function () {
      inputElevation
        .closest('.form__row')
        .classList.toggle('form__row--hidden');
      inputCadence.closest('.form__row').classList.toggle('form__row--hidden');
      inputType.blur();
    });
  }
  _newWorkout(e) {
    e.preventDefault();

    let typeSpecification = inputType.value;
    let data;
    let emoji;
    let today = new Intl.DateTimeFormat('en-US', {
      day: 'numeric',
      month: 'long',
    }).format(new Date());
    let distance = +inputDistance.value;
    let Duration = +inputDuration.value;

    let checker = (...inputs) => inputs.every(mov => Number.isFinite(mov));
    let PositiveChecker = (...inputs) => inputs.every(mov => mov > 0);

    if (typeSpecification === 'running') {
      emoji = '🏃‍♂️';
      let cadence = +inputCadence.value;
      if (
        !checker(distance, Duration, cadence) ||
        !PositiveChecker(distance, Duration, cadence)
      ) {
        alert('Enter a Valid And Positive Number');
        return;
      }
      data = new Running(coordinates, distance, Duration, cadence);
    }
    if (typeSpecification === 'cycling') {
      emoji = '🚴‍♀️';
      let elevation = +inputElevation.value;
      if (
        !checker(distance, Duration, elevation) ||
        !PositiveChecker(distance, Duration)
      ) {
        alert('Enter a Valid And Positive Number');
        return;
      }
      data = new Cycling(coordinates, distance, Duration, elevation);
    }

    if (!form.classList.contains('hidden')) {
      L.marker(coordinates, {
        opacity: 0.7,
        draggable: true,
        riseOnHover: true,
        icon: Icon,
      })
        .addTo(Application._returnMap())
        .bindPopup(
          L.popup({
            maxWidth: 250,
            minWidth: 100,
            autoClose: false,
            closeOnClick: false,
            className:
              typeSpecification === 'running'
                ? 'running-popup'
                : 'cycling-popup',
          })
        )
        .setPopupContent(
          `${emoji} ${
            typeSpecification[0].toUpperCase() + typeSpecification.slice(1)
          } on ${today}`
        )
        .openPopup();
    }
    form.style.display = 'none';
    form.classList.add('hidden');
    setTimeout(() => (form.style.display = 'grid'), 1000);
    if (inputDistance.value && inputDuration.value) {
      this.#DataArr.push(data);
      this._renderWorkout(data);
    }

    [...document.querySelectorAll('.form__input')]
      .slice(1)
      .forEach(mov => (mov.value = ''));
    this._setLoaclly();
  }
  _renderWorkout(data) {
    let text = `<li class="workout workout--${data.type}" data-id="${data.UID}">
    <h2 class="workout__title">${
      data.Description
    } <img src="outline_tune_white_24dp.png" alt="" class="edit--img"></h2>
    <div class="workout__details">
      <span class="workout__icon">${
        data.type === 'running' ? '🏃‍♂️' : '🚴‍♀️'
      }</span>
      <span class="workout__value">${data['Distance Covered']}</span>
      <span class="workout__unit">km</span>
    </div>
    <div class="workout__details">
      <span class="workout__icon">⏱</span>
      <span class="workout__value">${data.Duration}</span>
      <span class="workout__unit">min</span>
    </div>
    <div class="workout__details">
      <span class="workout__icon">⚡️</span>
      <span class="workout__value">${
        data.type === 'running' ? Math.round(data.Pace) : Math.round(data.Speed)
      }</span>
      <span class="workout__unit">${
        data.type === 'running' ? 'min/km' : 'km/h'
      }</span>
    </div>
    <div class="workout__details">
      <span class="workout__icon">${data.type === 'running' ? '🦶🏼' : '⛰'}</span>
      <span class="workout__value">${
        data.type === 'running' ? data.Cadence : data.ElevationGain
      }</span>
      <span class="workout__unit">${
        data.type === 'running' ? 'spm' : 'm'
      }</span>
    </div>
    
    </li>
    `;
    // document.querySelector('.workouts').insertAdjacentHTML('beforeend', text);
    document.querySelector('.form1').insertAdjacentHTML('afterend', text);
  }
  _Display() {
    console.log(this);
    console.log(this.#Usercoordinates);
  }
  _MoveToPopUp(e) {
    let element = e.target.closest('.workout');
    if (!element) return;

    let WorkoutID = this.#DataArr.find(mov => element.dataset.id === mov.UID);
    // console.log(WorkoutID.UID);

    this.#map.setView(WorkoutID['Marked Coordinates'], 17, {
      animate: true,
      pan: {
        duration: 1,
      },
    });
    if (WorkoutID._click) WorkoutID._click();
    //initially we cannot use because the prototype inheritance is not followed in the storage because the data is stored in the formed of string and afterwards when we extract it the prototypal chain breaks and a simple object is returned.
  }

  _setLoaclly() {
    localStorage.setItem('workouts', JSON.stringify(this.#DataArr));
  }
  _getData() {
    let data = JSON.parse(localStorage.getItem('workouts'));
    return data;
  }
  _DataArr() {
    return this.#DataArr;
  }
  _initialLoad() {
    let data = JSON.parse(localStorage.getItem('workouts'));
    if (!data) return;
    this.#DataArr = [...data];

    data.forEach(data => {
      this._renderWorkout(data);
    });
  }
  _editorLoad() {
    this.#DataArr.forEach(data => {
      this._renderWorkout(data);
    });
  }

  _initialMarker() {
    let data = JSON.parse(localStorage.getItem('workouts'));
    if (!data) return;

    data.forEach(data => {
      L.marker(data['Marked Coordinates'], {
        opacity: 0.7,
        draggable: true,
        riseOnHover: true,
      })
        .addTo(this._returnMap())
        .bindPopup(
          L.popup({
            maxWidth: 250,
            minWidth: 100,
            autoClose: false,
            closeOnClick: false,
            className:
              data.type === 'running' ? 'running-popup' : 'cycling-popup',
          })
        )
        .setPopupContent(
          `${data.type === 'running' ? '🏃‍♂️' : '🚴‍♀️'} ${data.Description}`
        )
        .openPopup();
    });

    let { Latitude, Longitude } = this.#Usercoordinates;
    this._returnMap().setView([Latitude, Longitude], 17);
  }
  reset() {
    localStorage.removeItem('workouts');
    location.reload();
  }
}
let Application = new App();

window.addEventListener('load', function () {
  console.log('hello window');
});
setTimeout(() => {
  Application._initialMarker();
}, 500);
// document.querySelector('body').addEventListener('keydown', function (e) {
//   console.log(this);

//   //here this keyword is the one to which we are attaching the event Listener
// });

let running1 = new Running([78, 20], 40, 50, 344);
console.log(running1);

[...document.querySelectorAll('.edit--img')].forEach(mov => {
  mov.addEventListener('click', function (e) {
    let dataBox = e.target.closest('.workout');
    if (EditorData?.UID === dataBox.dataset.id) {
      document.querySelector('.form1').classList.add('hidden');
    }
    if (EditorData?.UID !== dataBox.dataset.id) {
      document.querySelector('.form1').classList.remove('hidden');
    }

    let data = Application._getData().find(
      mov => mov.UID === dataBox.dataset.id
    );
    EditorData = data;
  });
});

document.querySelector('.form1').addEventListener('submit', function (e) {
  e.preventDefault();

  Application._DataArr().forEach(data => {
    if (data.UID === EditorData.UID) {
      data.Duration = +document.querySelector('.form__input--editor--duration')
        .value;
      data.Cadence = +document.querySelector('.form__input--editor--cadence')
        .value;

      data['Distance Covered'] = document.querySelector(
        '.form__input--editor--distance'
      ).value;
    }
  });
  Application._editorLoad();
  Application._setLoaclly();
  console.log(document.querySelector('.form__input--editor--type').value);
  document.querySelector('.form1').classList.add('hidden');
});
