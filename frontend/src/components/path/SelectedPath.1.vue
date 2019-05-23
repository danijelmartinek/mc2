<template>
    <div id="selectedPath">
       <div id="toggleCategoryContainer">
        <div id="toggleCategory">
            <label class="select">
                <input type="radio" checked="checked" name="radio">
                <span class="checkmark"></span>
                <div class="text">Gimnazija IZD</div>
            </label>
            <div class="dots">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <label class="select">
                <input type="radio" name="radio">
                <span class="checkmark"></span>
                <div class="text">Tehničko Veleučilište u Zagrebu</div>
            </label>
            <div class="dots">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <label class="select">
                <input type="radio" name="radio">
                <span class="checkmark"></span>
                <div class="text">Web developer</div>
            </label>
        </div>
        </div>
    </div>
</template>

<style>
#selectedPath{
    width: 100%;
    height: 100%;

    background-color: green;
}

@media only screen and (min-width: 1070px) {

    #selectedPath{
        position: fixed;
        width: 80%;
        margin-left: 20%;
    }
}


#toggleCategoryContainer{
  position: fixed;
  height: 100%;
  width: 200px;
  right: 0;
  
  background-color: blue;
}

#toggleCategory{
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  right: -75%;
  padding: 1em;
}

#toggleCategory:checked{
  right: 0%;
}


.select {
  display: inline-block;
  position: relative;
  margin: 0.5em 0.15em 1.5em 0.15em;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.text {
  position: absolute;
    display: block;
  padding-left: 35px;
  font-size: 1em;
  text-transform: uppercase;
}

/* Hide the browser's default radio button */
.select input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

/* Create a custom radio button */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 20px;
  width: 20px;
  background-color: #eee;
  border-radius: 50%;
}

/* On mouse-over, add a grey background color */
.select:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the radio button is checked, add a blue background */
.select input:checked ~ .checkmark {
  background-color: #FF0000;
  box-shadow: 1px 1px 7px #FF6347;
}

.dots{
	width: 10px;
}

.dots > span{
  height: 10px;
  width: 10px;
  margin: 0.5em 0.5em 0.5em 0.5em;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
</style>
