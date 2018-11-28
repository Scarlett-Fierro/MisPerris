var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/formulario/',
    '/listar-mascotas/',
    '/formulario-mascota/',
    '/accounts/login/',
    '/accounts/register/',
    // 'https://fonts.googleapis.com/css?family=Codystar', FUENTE QUE NO SE MUESTRA
    '/static/core/css/estilos.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/social-inst.png',
    '/static/core/img/logo.png',
    '/static/core/img/rescate.jpg',
    '/static/core/img/crowfunding.jpg',
    '/media/media/RESCATADO2_XWif5Xo.png',
    '/media/media/RESCATADO3_cTHh7ym.jpg',
    '/media/media/RESCATADO4.jpg',
    '/media/media/AdoptadoNavidad.jpg',
    '/media/media/AdoptadoDormido.jpg',
    '/media/media/AdoptadoBolsillo.jpg',
    '/media/media/AdoptadoFlojo.jpg'
    
];

/*
    '/formulario-mascota/',
    '/accounts/login/',
    '/listar-mascotas/',
    '/formulario-mascota/',
    '/accounts/register/',
*/

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
           /* r = null
            fetch(event.request)
            .then(function() {
                
            })
            .catch(function() {
                r = response;
            })

            if(response) {
                return response;
            }*/
            
            return fetch(event.request).catch(function() {
                console.log("no funciona")
                return response;
            });
        })
    );

});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyCXx90-U1o8m-229WtLhy9j7uiN3OShgGY",
    authDomain: "misperris-93ffb.firebaseapp.com",
    databaseURL: "https://misperris-93ffb.firebaseio.com",
    projectId: "misperris-93ffb",
    storageBucket: "misperris-93ffb.appspot.com",
    messagingSenderId: "182082072387"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

//Programamos una funcion que estara escuchando cuando llegue una notificacion desde Firebase

messaging.setBackgroundMessageHandler(function(){
    //El playload contendra el mensaje destinado al usuario
    var title = "Notificacion"
    var options = {
        body:"Este es el cuerpo del mensaje"
    }

    //Mostramos la notificacion al usuario
    return self.registration.showNotification(title, options);

})
