<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <div>
            <div style="text-align: center;">
                <div style="font-size: 4em; margin: 0.5em 0em 0.5em 0em; color: #FF5E3A;"><font-awesome-icon icon="check" /></div>
                <div class="title">Uspješno ste se registrirali!</div>
            </div>
            <br>
            <div>

                <button class="btn" @click="close()">
                    OK
                </button>
            </div>
        </div>

      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'modal',
    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>

<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgb(44, 54, 93, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    width: 90%;
    background: #FFFFFF;
    border-radius: 1em;
	box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.2);
    overflow-x: auto;
    display: flex;
    flex-direction: column;
}

@media only screen and (min-width: 710px) {
	.modal {
		width: 70%;
	}
}

@media only screen and (min-width: 1070px) {
	.modal {
		width: 50%;
	}
}

@media only screen and (min-width: 1610px) {
	.modal {
		width: 30%;
	}
}

.modal-fade-enter,
.modal-fade-leave-active {
    opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity .2s ease
}

.title{
    text-transform: uppercase;
    font-weight: bold;
    font-size: 1.3em;
    color: #2c365d;
}

.btn {
	float: right;
	width: auto !important;
	color: #F2F2F0;
	font-weight: bold;
	text-transform: uppercase;
	cursor: pointer;
	background-color: #FF5E3A;
	padding: 1em;
}

.btn:active {
	opacity: 0.8;
}
</style>