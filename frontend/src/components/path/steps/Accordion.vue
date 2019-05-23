<template>
    <div>
        <div class="wrap-collabsible">
            <input :id="accordionID" class="toggle" type="checkbox">
            <label :for="accordionID" class="lbl-toggle" :style="{'width': width}"><span>{{label}}</span></label>
            <div class="collapsible-content">
                <div class="content-inner">
                    <slot></slot>
                </div>
            </div>
        </div>
	</div>   
</template>

<script>
export default {
    name: 'accordion',
    props: ['label', 'width', "accordionID"],
    mounted(){

        let myLabels = document.querySelectorAll('.lbl-toggle');

        Array.from(myLabels).forEach(label => {
            label.addEventListener('keydown', e => {
                // 32 === spacebar
                // 13 === enter
                if (e.which === 32 || e.which === 13) {
                e.preventDefault();
                label.click();
                }
            })
        })
    }
}
</script>

<style scoped>
.wrap-collabsible {
    margin-bottom: 1.2rem 0;
}

input[type='checkbox'] {
    display: none;
}

.lbl-toggle {
    display: inline-block;

    font-weight: bold;
    font-family: monospace;
    font-size: 1.2rem;
    text-transform: uppercase;
    text-align: center;

    padding: 1rem;

    color: #fff;
    background: #0a2155;

    cursor: pointer;

    border-radius: 7px;
    transition: all 0.25s ease-out;
}

.lbl-toggle > span {
    float: left;
}

.lbl-toggle:hover {
    color: #f54925;
}

.lbl-toggle::before {
    float: left;
    content: ' ';
    display: inline-block;
    margin-top: 0.3em;

    border-top: 5px solid transparent;
    border-bottom: 5px solid transparent;
    border-left: 5px solid currentColor;
    vertical-align: middle;
    margin-right: .7rem;
    transform: translateY(-2px);

    transition: transform .2s ease-out;
}

.toggle:checked + .lbl-toggle::before {
    transform: rotate(90deg) translateX(-3px);
}

.collapsible-content {
    max-height: 0px;
    overflow: hidden;
    transition: max-height .25s ease-in-out;
}

.toggle:checked + .lbl-toggle + .collapsible-content {
    max-height: 100%;
}

.toggle:checked + .lbl-toggle {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.collapsible-content .content-inner {
    background: #0a2155;
    border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;
    padding: .5rem 1rem;
}   
</style>
