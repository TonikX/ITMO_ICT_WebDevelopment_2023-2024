import { defineStore } from "pinia";
import { capsulesApi, commentsApi } from "@/api";
import usersStore from "@/stores/user.js";

const capsulesStore = defineStore("capsules", {
    state: () => ({
        capsules: [],
        capsule: {
            "name":"NoneCap",
            "openDate":1701644520000,
            "description":"None",
            "access":false,
            "text":"None",
            "files":[],
            "userId": undefined,
            "userName": "None",
            "id": undefined,
        },
        selector: "All",
    }),

    actions: {
        async loadCapsules() {
            let usStore = usersStore()
            const accessToken = usStore.token
            if( accessToken !== "" ) {
                const user = usStore.user
                if (this.selector === "My") {
                    const response = await capsulesApi.getMyCapsules(user['id'], accessToken);
                    this.capsules = response.data;
                    return response;
                }
                if (this.selector === "notMy") {
                    const response = await capsulesApi.getNotMyCapsules(user['id'], accessToken);
                    this.capsules = response.data;
                    return response;
                }
            }
            if(this.selector === "All"){
                const response = await capsulesApi.getAllCapsules();
                this.capsules = response.data;
                //console.log("AllCap", this.capsules)
                return response;
            }
            if(this.selector === "opened"){
                const response = await capsulesApi.getOpenedCapsules();
                this.capsules = response.data;
                return response;
            }
            if(this.selector === "closed"){
                const response = await capsulesApi.getClosedCapsules();
                this.capsules = response.data;
                return response;
            }
        },

        async createCapsule(data) {
            let usStore = usersStore()
            const accessToken = await usStore.token
            if(data['access']){
                data['access'] = "ffa";
            }
            else{
                data['access'] = "my";
            }
            data['owner'] = await (usStore.user)['id']
            //console.log(data)
            await capsulesApi.createCapsule(data, accessToken);
            //this.capsules = response.data;
            //return response;
        },

        async loadOneCapsule(id){
            let usStore = usersStore()
            const accessToken = usStore.token
            const userId = (usStore.user)['id']
            const response = (await capsulesApi.getOneCapsule(id, userId, accessToken));
            //console.log(response.data)
            //console.log(response)
            this.capsule = response.data
            //console.log("Store", this.capsule)
            return response;
        },

        async loadComments(vaultId){
            let usStore = usersStore()
            const accessToken = usStore.token
            const response = (await commentsApi.getVaultComments(vaultId, accessToken));
            this.capsule.comments = response.data
        },

        async createComment(data){
            let usStore = usersStore()
            const accessToken = usStore.token
            const user = usStore.user
            data.person = user['id']
            console.log(data)
            await commentsApi.createComments(data, accessToken)
            //await this.loadComments();
        }
    },
});

export default capsulesStore;