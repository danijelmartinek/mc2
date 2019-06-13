<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <slot></slot>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'modal'
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

.modal-fade-enter,
.modal-fade-leave-active {
    opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity .2s ease
}
</style>