<template>
    <div id="repository">
        <div class="main">
            <div class="title">Moji predmeti</div>
            <span class="line"></span>
            <div class="subject">
                <span class="line-small"></span>
                <span class="sub">Matematika</span>
                <span>
                    <div class="year">2018.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
                <span>
                    <div class="year">2017.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
                <span>
                    <div class="year">2016.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
            </div>
            <div class="subject">
                <span class="line-small"></span>
                <span class="sub">Fizika</span>
                <span>
                    <div class="year">2018.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
                <span>
                    <div class="year">2017.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
                <span>
                    <div class="year">2016.</div>
                    <div class="files">
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                        <div class="file-item"><font-awesome-icon :icon="['far', 'file-pdf']" /><span>zadaci.pdf</span></div>
                    </div>
                </span>
            </div>
        </div>
	</div>   
</template>

<script>

export default {
	data() {
		return {

		}
    },
    mounted(){

    }
}
</script>

<style scoped>
.main{
    height: 100%;
    width: 100%;
    color: #2C365D;
    background-color: #fff;
    padding-bottom: 10em;
}

@media only screen and (min-width: 1070px) {
    .main {
        height: 100vh; 
        overflow-x: hidden; 
        overflow-x: auto;
    }
}

.main > .title{
    width: 50%;
    font-size: 2em;
    text-align: right;
    padding: 1em 0em 0.5em 1em;
    font-weight: bold;
    text-transform: uppercase;
}

@media only screen and (min-width: 1070px) {
    .main {
        height: 100vh; 
    }
}

.line{
    display: block;
    width: 50%;
    height: 5px;
    background-color: #FF5E3A;
    margin-bottom: 1em;
}

.line-small{
    float: left;
    width: 20%;
    height: 1.4em;
    margin-left: -2em;
    background-color: #FF5E3A;
}

.subject{
    padding: 1em;
    margin: 2em;
    border-radius: 2em;
    color: #F2F2F0;
    font-weight: bold;
    background-color: #2C365D;
}

@media only screen and (min-width: 1070px) {
    .subject {
        margin: 5em; 
    }
}

.subject > .sub{
    margin-left: 1em;
    font-size: 1.2em;
}

.subject > span > .year{
    padding: 2em 0em 0em 1em;
}

.subject > span > .files{
    padding: 0.5em 0em 1em 3em;
}

.file-item{
    padding: 0.3em;
}

.file-item > span{
    padding-left: 0.5em;
    text-decoration: underline;
}
</style>