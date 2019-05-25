<template>
    <div>
        <div class="wrap-collabsible" :style="customStyleWrap">
            <input :id="accordionID" class="toggle" type="checkbox">
            <label :for="accordionID" class="lbl-toggle" :style="{'width': width}"><i class="arrow"></i><span>{{label}}</span></label>
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
    props: ['label', 'width', "accordionID", 'customStyleWrap'],
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

    font-family: monospace;
    font-size: 1.2rem;
    text-transform: uppercase;
    text-align: center;

    padding: 1rem;

    color: #2C365D;

    cursor: pointer;

    border-radius: 7px;
    transition: all 0.25s ease-out;
}

.lbl-toggle > span {
    float: left;
    text-align: left;
}

.lbl-toggle:hover {
    color: #FF5E3A;
}

.lbl-toggle:hover .arrow {
    border-color: #FF5E3A;
}

.lbl-toggle i {
    display: block;
    float: left;
    height: 100%;
    margin: 0.3em 0.7em 0.7em 0em;
    border: solid #2C365D;
    border-width: 0 3px 3px 0;
    display: inline-block;
    padding: 3px;

    transition: all 0.25s ease-out;
}

.lbl-toggle .arrow {
  transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
}

.toggle:checked + .lbl-toggle .arrow {
    transform: rotate(45deg) translateX(-3px);
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
    background: #F2F2F0;
    border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;
    padding: .5rem 1rem;
}   
</style>
