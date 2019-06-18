<template>  
    <div class="timeline-container">
        <div class="timeline-wrap">
            <ol class="timeline">
                <div class="title">Rokovi</div>
                <li class="timeline__entry">
                    <time>
                    do 15.2.2019. 
                    <br>
                    12:00h
                    </time>
                    <h3 class="timeline__headline">
                    Prijava ispita državne mature.
                    </h3>
                </li>
                <li class="timeline__entry notsoimportant">
                    <time>
                    do 16.2.2019. 
                    </time>
                    <h3 class="timeline__headline">
                    Dostava zahtjeva za prilagodbu ispitne tehnologije.
                    </h3>
                </li>
                <li class="timeline__entry notsoimportant">
                    <time>
                    do 27.2.2019. 
                    </time>
                    <h3 class="timeline__headline">
                    Dostava dokumentacije centru.
                    </h3>
                </li>
                <li class="timeline__entry">
                    <time>
                    do 3.5.2019. 
                    </time>
                    <h3 class="timeline__headline">
                        Uplata ispita državne mature.
                    </h3>
                    <h3 class="timeline__headline notsoimportant">
                        <li>Naknadna prijava – <b>samo iz opravdanih razloga</b></li>
                        <br>
                        <li>Promjena prijavljenih ispita – <b>samo iz opravdanih razloga</b></li>
                    </h3>
                </li>
                <li class="timeline__entry">
                    <time>
                    do 14.5.2019. 
                    </time>
                    <h3 class="timeline__headline">
                    Odjava prijavljenih ispita.
                    </h3>
                </li>
                <li class="timeline__entry">
                    <time>
                    do 25.5.2019. 
                    </time>
                    <h3 class="timeline__headline">
                    Dostava svjedodžbe o završenom 4. razredu ako kandidat završava 4.razred
                    </h3>
                </li>
                <li class="timeline__entry">
                    <time>
                    do 2.7.2019. 
                    </time>
                    <h3 class="timeline__headline">
                    Dostava završne svjedodžbe
                    </h3>
                </li>

            </ol>
        </div>

        <div class="timeline-wrap">
            <ol class="timeline">
                <div class="title">Matura - ljetni rok</div>

                <li class="timeline__entry">
                    <time>
                        17.6.2019. 
                    <br>
                    09:00h
                    </time>
                    <h3 class="timeline__headline">
                    Hrvatski jezik A
                    </h3>
                </li>

                <li class="timeline__entry">
                    <time>
                        19.6.2019. 
                    <br>
                    09:00h
                    </time>
                    <h3 class="timeline__headline">
                      Engleski jezik
                    </h3>
                </li>

                <li class="timeline__entry">
                    <time>
                        26.6.2019. 
                    <br>
                    09:00h
                    </time>
                    <h3 class="timeline__headline">
                      Matematika
                    </h3>
                </li>

            </ol>
        </div>
    </div>
</template>

<style scoped>
.timeline-container {
    margin-top: 0;
    position: static;
}

@media only screen and (min-width: 1070px) {
    .timeline-container {
        height: 100vh; 
        overflow-x: hidden; 
        overflow-x: auto;
    }
}

.timeline-container * {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

.timeline-container *::before, *::after {
  box-sizing: inherit;
}

.timeline-container {
  font-weight: 400;
  font-size: 10px;
  background-color: #F2F2F0;
  color: #2C365D;
}

.timeline-container {
  font-size: 1rem;
}

@media only screen and (min-width: 768px) {
  .timeline-container {
    font-size: 1.2rem;
  }
}

@media only screen and (min-width: 1025px) {
  .timeline-container {
    font-size: 1.4rem;
  }
}

.timeline-wrap {
  max-width: 1000px;
  padding: 2.5rem 1.25rem;
  margin: 0 auto;
}

.timeline {
  position: relative;
  list-style-type: none;
  padding-bottom: 5rem;
}

.timeline > *:not(:last-child) {
  margin-bottom: 5rem;
}

.timeline > .title {
  position: relative;
  z-index: 1;
  display: inline-block;
  background-color: #FF5E3A;
  color: #F2F2F0;
  padding: 10px 40px;
  margin-bottom: 5rem;
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
}

@media only screen and (min-width: 768px) {
  .timeline > .title {
    border-radius: 25px;
    left: 50%;
    transform: translateX(-50%);
  }
}

.timeline::after {
  content: ' ';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 2px;
  background-color: #2C365D;
  opacity: 0.15;
}

@media only screen and (min-width: 768px) {
  .timeline::after {
    left: 50%;
    transform: translateX(-50%);
  }
}

.timeline time {
  display: inline-block;
  font-weight: 700;
  color: #FF5E3A;
}

.timeline__entry {
  position: relative;
}

.timeline__entry > *:not(:last-child) {
  margin-bottom: 2rem;
}

@media only screen and (max-width: 767px) {
  .timeline__entry {
    padding-left: 5rem;
  }
}

@media only screen and (min-width: 768px) {
  .timeline__entry {
    width: 50%;
  }

  .timeline__entry:nth-of-type(odd) {
    text-align: right;
    padding-right: 5rem;
    margin-right: auto;
  }

  .timeline__entry:nth-of-type(odd)::before {
    left: auto;
    right: -8px;
  }

  .timeline__entry:nth-of-type(odd)::after {
    left: auto;
    right: 0;
  }

  .timeline__entry:nth-of-type(even) {
    padding-left: 5rem;
    margin-left: auto;
  }
}

.timeline__entry::before, .timeline__entry::after {
  content: ' ';
  position: absolute;
  margin-top: 1rem;
}

.timeline__entry::before {
  width: 16px;
  height: 16px;
  top: 1px;
  left: -8px;
  z-index: 2;
  background-color: #F2F2F0;
  border: 3px solid #FF5E3A;
  border-radius: 50%;
  transform: translateY(-50%);
}

.timeline__entry::after {
  width: 35px;
  height: 2px;
  top: 0;
  left: 0;
  z-index: 1;
  background-color: #FF5E3A;
}

.timeline__headline {
  font-size: 1.2rem;
  color: #2C365D;
}

.timeline__list {
  display: inline-block;
  list-style-position: inside;
  list-style-type: disclosure-closed;
  line-height: 1.6;
}

.notsoimportant{
    font-weight: 200;
}

.notsoimportant > time{
    font-weight: 300;
}

.notsoimportant > h3{
    font-weight: 200;
}
</style>

