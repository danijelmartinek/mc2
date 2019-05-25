<template>
    <div class="autocomplete">
        <p class="control icon-right">
        <input type="text" class="input-dropdown"
        :placeholder="placeholder"
        @input="onInput($event.target.value)" 
        @blur="isOpened = false"
        @keyup.enter="select"
        @keyup.tab="select"
        @keydown.down="onDown"
        @keydown.up="onUp"
        @keyup.esc="isOpen = false"
        ref="dropdown"
        v-model="search"
        />
        <i class="chevron bottom" 
            @click="toggle"
            :class="{'chevron-active' : isOpened, 'chevron-inactive' : !isOpened}"></i>
        </p>
        <transition	name="fade" mode="in-out">
            <ul class="options-list" v-show="isOpened">
                <li 
                    v-for="(option, i) in filteredItems" :key="i"
                    @mouseenter="selected = i"
                    @mousedown="select"
                    :class="{'selected': i === selected}"
                >
                    {{ option.naziv }}
                    <slot name="item" :title="option.naziv" :thumbnail="option.thumbnail"></slot>
                </li>
                <li v-if="!(filteredItems.length > 0)">{{ noitems }}</li>
            </ul>
        </transition>
    </div>
</template>

<script>
export default {
    data() {
    return {
      isOpened: false,
      selected: null,
      search: ""
    };
  },
  props: {
    options: {
      type: Array,
      required: true
    },

    placeholder: {
      type: String,
    },

    noitems: {
      type: String,
    }
  },
  methods: {
    onInput(value) {
      this.isOpened = !!value; //(value != '');
      this.selected = -1;
    },
    select() {
        if(this.selected){
            const selectedOption = this.filteredItems[this.selected];
            this.$emit("select-item", selectedOption);
            this.search = selectedOption.naziv;
            this.isOpened = false;
        } else if(this.filteredItems[0]) {
            const selectedOption = this.filteredItems[0];
            this.$emit("select-item", selectedOption);
            this.search = selectedOption.naziv;
            this.isOpened = false;
        }
    },  
    onDown() {
      if (!this.isOpened) {
        return;
      }
      this.selected = (this.selected + 1) % this.filteredItems.length;
    },
    onUp() {
      if (!this.isOpened) {
        return;
      }

      this.selected =
        this.selected - 1 < 0
          ? this.filteredItems.length - 1
          : this.selected - 1;
    },
    toggle() {
      this.isOpened = !this.isOpened;
      this.search = ""
      if (this.isOpened) {
        this.$refs.dropdown.focus();
      }
    }
  },
  computed: {
    filteredItems() {
      const condition = new RegExp(this.search, "i");
      return this.options.filter(item => item.naziv.match(condition));
    }
  }
}
</script>

<style scoped>

.autocomplete {
  width: 600px;
}
ul.options-list li.selected {
  background-color: #fff;
  color: #f54925;
}

input.input-dropdown {
  font-family: "Nunito", Helvetica, Arial, sans-serif;
  height: 40px;
  width: 100%;
  border: 1px solid #fff;
  border-radius: 2px 0 0 2px;
  background-color: #fff;
  border-radius: 5px 5px 0px 0px;
  color: #000;
  font-size: 16px;
  padding-right: 38px;
  padding-left: 8px;
}

input.input-dropdown::-webkit-input-placeholder {
  color: #000;
}

input.input-dropdown::placeholder{
    color: #7e7e7e;
}

input.input-dropdown:focus::placeholder{
    color:transparent;
}


p.control {
  position: relative;
  display: flex;
  margin-bottom: 0.1rem;
    border: 1px solid #7e7e7e;
    border-radius: 5px 5px 0px 0px;
  z-index: 10;
}

p.control i {
  width: 70px;
  top: 0;
  border: none;
  right: 0;
  color: #f54925;
  border-radius: 5px 5px 0px 0px;
  box-shadow: -2px 0px 1px #fff;
  border-radius: 0 2px 2px 0;
}

ul.options-list {
    position: absolute;
    z-index: 200;
    min-width: 600px;
  list-style-type: none;
  padding: 0;
  margin: 0;
  border: 1px solid #dbdbdb;
  border-radius: 0 0 3px 3px;
  max-height: 300px;
  overflow-y: auto;
  box-shadow: 0px 3px 6px 0px rgba(195, 195, 195, 0.76);
}

ul.options-list li {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  justify-content: flex-end;
  padding: 0.4rem;
  border-bottom: 1px solid #eee;
  color: #7e7e7e;
  background-color: #fff;
  cursor: pointer;
}
.icon-right i:hover,
i.chevron.bottom.chevron-active {
 color: #fff;
  box-shadow: 0 0 6px #fff;
  background-color: #f54925;
}

ul.options-list li span {
  margin-right: 4px;
}

.chevron:before {
  border-style: solid;
  border-width: 0.25em 0.25em 0 0;
  content: "";
  display: inline-block;
  height: 0.45em;
  left: 0.05em;
  position: relative;
  top: 0.15em;
  transform: rotate(-45deg);
  vertical-align: top;
  width: 0.45em;
  transition: 0.3s all ease;
  will-change: transform;
}

.chevron.bottom:before {
  top: 16px;
  left: 19px;
}

.chevron-active.bottom:before {
  transform: rotate(135deg);
  will-change: transform;
}

.chevron-inactive.bottom:before {
  transform: rotate(225deg);
  will-change: transform;
}

ul.options-list li:last-child {
  border-bottom: none;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
  will-change: opacity;
  transform: translateY(-30px);
}
</style>
