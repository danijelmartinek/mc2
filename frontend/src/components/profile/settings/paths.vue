<template>
    <div id="paths">
        <span v-if="$store.state.user.savedPaths[0]">
            <div class="sPath row" v-if="pathDataLoaded">
                <div class="heading">Odabrani put <div class="delete" @click="deletePath()"><font-awesome-icon :icon="['fa', 'trash-alt']" /></div></div>
                <div><span class="k">Fakultet: </span><span class="p">{{ selectedPath.fakultet.naziv }}</span></div>
                <div><span class="k">Zanimanje: </span><span class="p">{{ selectedPath.zanimanje.naziv }}</span></div>
            </div>
            <div class="divider"></div>
            <div class="allPaths drow">
                <div class="heading">Spremljeni putevi</div>
                <div class="dcol xs-12 m-6 l-4" v-for="(path, index) in savedPaths" :key="index">
                    <div @click="selectPath(index)">
                        <div class="sPath">
                            <div><span class="k">Fakultet: </span><span class="p">{{ path.fakultet.naziv }}</span></div>
                            <div><span class="k">Zanimanje: </span><span class="p">{{ path.zanimanje.naziv }}</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </span>
        <span v-else>
            <div class="heading">Nemaš spremljenih puteva.</div>
        </span>
	</div>   
</template>

<script>
import axios from "axios"

export default {
    name: 'paths',
	data() {
		return {
            selectedPath: {},
            savedPaths: [],
            selectedIndex: 0
		}
    },
    mounted(){
        if(this.$store.state.user.savedPaths[0]){
            let selectedPathId = [this.$store.state.user.selectedPath]
            this.getPath(selectedPathId)

            let savedPathsId = this.$store.state.user.savedPaths
            this.getSavedPaths(savedPathsId)
        }
    },
    methods:{
        getPath(arr){
            let headers = {
                'Content-Type': 'application/json'
            }

            axios.post('/api/getpaths', arr, {headers: headers})
            .then(res => {
                if(res.status == 200){
                    this.selectedPath = res.data[0]
                }
            })
        },

        getSavedPaths(arr){
            let headers = {
                'Content-Type': 'application/json'
            }

            axios.post('/api/getpaths', arr, {headers: headers})
            .then(res => {
                if(res.status == 200){
                    this.savedPaths = res.data

                    let t = this
                    setTimeout(function(){
                        t.savedPaths.forEach((p, ind) => {
                            if(p._id == t.selectedPath._id){
                                t.selectPath(ind)
                            }
                        })
                    }, 50)
                }
            })
        },

        selectPath(i){
            if(this.$store.state.user.savedPaths[0]){
                let elems = document.getElementsByClassName("allPaths")[0].getElementsByClassName("dcol")
                for(let x = 0; x < elems.length; x++){
                    elems[x].classList.remove("pathSelected")
                }

                this.selectedPath = this.savedPaths[i]
                elems[i].classList.add("pathSelected")

                let obj = {
                    _id: this.$store.state.user._id,
                    selectedPath: this.savedPaths[i]._id,
                    savedPaths: this.$store.state.user.savedPaths
                }

                let headers = {
                    'Content-Type': 'application/json'
                }

                axios.post('/api/updatesavedpaths', obj, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        this.selectedIndex = i
                        this.$store.state.user.selectedPath = this.savedPaths[i]._id
                    }
                })
            } else {
                let obj = {
                    _id: this.$store.state.user._id,
                    selectedPath: "",
                    savedPaths: []
                }

                let headers = {
                    'Content-Type': 'application/json'
                }

                axios.post('/api/updatesavedpaths', obj, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        this.$store.state.user.selectedPath = ""
                        this.$store.state.user.selectedStudy = ""
                        this.$store.state.user.selectedPath = []
                    }
                })
            }
        },

        deletePath(){
            this.savedPaths.splice(this.selectedIndex, 1)
            this.$store.state.user.savedPaths.splice(this.selectedIndex, 1)
            this.selectPath(0)
        }
    },
    computed:{
        pathDataLoaded(){
            if(this.selectedPath._id){
                return true
            } else {
                return false
            }
        }
    }
}
</script>

<style scoped>
.sPath > div{
    padding-top: 0.5em;
}

.heading{
    font-size: 1.3em;
    font-weight: bold;
}

.sPath .k{
    text-transform: uppercase;
    font-weight: bold;
}
.sPath .p{
    text-transform: capitalize;
}

.allPaths > div{
    padding: 0.5em;
}

.allPaths > div > div{
    min-height: 150px;
    background-color: #2C365D;
    color: #F2F2F0;
    padding: 1em;
    border-radius: 1em;
    cursor: pointer;
}

.pathSelected > div{
    background-color: #fd7d61 !important;
}

.divider {
    margin: 1em 0em 1em 0em;
    width: 100%;
    height: 2px;
    background-color: #fd7d61;
}

.delete{
    float: right;
    font-size: 1.2em;
    cursor: pointer;
}

.delete:hover{
    color: #fd7d61;
}
</style>