<template>
  <section ref="styles" style="display:none;">
    <slot></slot>
  </section>
</template>

<script>
export default {
  name: 'custom-styles',
  props: [],
  data () {
    return {
    }
  },
  mounted: function() {
    let styleTag = document.createElement('style');
    styleTag.textContent = this.$refs.styles.textContent;
    this.$refs.styles.textContent = null;
    this.$refs.styles.appendChild(styleTag);
  }
}
</script>