<template>
    <div id="navigation">
        <div class="container">
            <div class="inner-container">
                <div class="item" v-for="(item, index) in items" :key="index" @click="select(index)">
                    <span>
                        <span class="icon"><font-awesome-icon :icon="item.icon" /></span>
                        <span class="text">{{ item.text }}</span>
                    </span>
                </div>
                <div class="dummy-item"></div>
            </div>
        </div>
	</div>   
</template>

<script>
export default {
    name: 'navigation',
    props: ['items'],
	data() {
		return {
            elements: document.getElementsByClassName('item'),
            selectedItem: 0
		}
    },
    mounted(){
        this.select(0)

        this.initStyle()
    },
    methods: {
        select(i){
            this.resetSelect(this.selectedItem)
            
            this.elements[i].classList.add("item-selected")

            if(i > 0){
                this.elements[i-1].classList.add("item-selected-b")
            }
            if(i < (this.elements.length - 1)){
                this.elements[i+1].classList.add("item-selected-a")
            } 
            if(i == (this.elements.length - 1)) {
                let dummyItem = document.getElementsByClassName('dummy-item')[0]
                dummyItem.classList.add("item-selected-a")
            }

            this.selectedItem = i
            this.$emit('changePage', i)
        },

        resetSelect(selectedIndex){

            this.elements[selectedIndex].classList.remove("item-selected")

            if(selectedIndex > 0){
                this.elements[selectedIndex - 1].classList.remove("item-selected-b")
            }
            if(selectedIndex < (this.elements.length - 1)){
                this.elements[selectedIndex + 1].classList.remove("item-selected-a")
            } 
            if(selectedIndex == (this.elements.length - 1)) {
                let dummyItem = document.getElementsByClassName('dummy-item')[0]
                dummyItem.classList.remove("item-selected-a")
            }
   
        },

        initStyle(){

            function widthHandler() {
                x = window.matchMedia("(min-width: 1070px)")
                let items = document.getElementsByClassName('item')

                if (x.matches) { // If media query matches
                    document.getElementsByClassName('inner-container')[0].style.height = 7 * (itemCount + 1) + "em"
                    for(let i = 0; i < items.length; i++){
                        items[i].style.width = 100 + "%"
                    }
                } else {
                    for(let i = 0; i < items.length; i++){
                        document.getElementsByClassName('inner-container')[0].style.height = 5 + "em"
                        items[i].style.width = 100 / itemCount + "%"
                    }
                }
            }

            const itemCount = this.items.length

            let x = window.matchMedia("(min-width: 1070px)")
            widthHandler()
             // Call listener function at run time
            window.addEventListener("resize", widthHandler) // Attach listener function on state changes

        }
    }
}
</script>

<style scoped>
.container{
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 4em;
    z-index: 999;

    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -o-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color:  rgba(255, 255, 255, 0); 
}

.inner-container{
    background-color: #F2F2F0;
}

.item {
    position: relative;
    float: left;
    width: 25%;
    height: 5em;
    background-color: #2C365D;
    cursor: pointer;
}

.item:hover {
    opacity: 0.8;
}

.item > span{
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
    color: #F2F2F0;
}

.item > span > .icon {
    font-size: 1.5em;
    display: block;
    text-align: center;
}

.item > span > .text {
    font-size: 0.8em;
    display: none;
}

.item-selected {
    background-color: #F2F2F0;
}

.item-selected > span {
    color: #2C365D;
}

.item-selected > span > .icon {
    font-size: 1.5em;
}

.item-selected > span > .text {
    display: block;
}

.item-selected-b {
    border-top-right-radius: 2em;
    background-color: #2C365D;
}
.item-selected-a {
    border-top-left-radius: 2em;
    background-color: #2C365D;
}

.dummy-item{
    display: none;
}

@media only screen and (min-width: 1070px) {

    .container{
        position: fixed;
        width: 7em;
        height: 92%;
        background-color: #2C365D;
        z-index: 999;
        box-shadow: 10px 0px 50px 10px rgba(0, 0, 0, 0.2);
    }

    .inner-container{
        height: 35em;
        background-color: #F2F2F0;
    }

    .item {
        position: relative;
        width: 100%;
        height: 7em;
        background-color: #2C365D;
        cursor: pointer;
        z-index: 200;
    }

    .item > span{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: bold;
        color: #F2F2F0;
    }

    .item:hover > span > .text {
        font-size: 0.8em;
        display: block;
    }

    .item > span > .icon {
        font-size: 1.5em;
        display: block;
        text-align: center;
    }

    .item > span > .text {
        display: none;
    }

    .item-selected {
        background-color: #F2F2F0;
        z-index: 0;
    }

    .item-selected > span {
        color: #2C365D;
    }

    .item-selected > span > .text {
        display: block;
    }

    .item-selected-b {
        border-top-right-radius: 0em;
        border-bottom-right-radius: 2em;
        background-color: #2C365D;
        z-index: 200;
        box-shadow: 0px 10px 10px 5px rgba(0, 0, 0, 0.2);
    }

    .item-selected-a {
        border-top-left-radius: 0em;
        border-top-right-radius: 2em;
        background-color: #2C365D;
        z-index: 200;
        box-shadow: 0px -10px 10px 5px rgba(0, 0, 0, 0.2);
    }

    .dummy-item{
        display: inline-block;
        position: relative;
        width: 100%;
        height: 7em;
        background-color: #2C365D;
    }

}
</style>