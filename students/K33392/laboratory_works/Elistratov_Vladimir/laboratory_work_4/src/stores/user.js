import { defineStore } from "pinia";
import { usersApi } from "@/api";

const usersStore = defineStore("users", {
    state: () => ({
        user: "",
        sideUser: "",
        friend: "",
        token: "",
    }),

    getters: {
        authCheck: state => {
          return (state.token !== "")
        },
        updateCheck: state => {
            return (state.user)
        }
    },

    actions: {
        async loginUser(data) {
            const response = (await usersApi.userLogin(data))['data'];
            await this.loadUserData(response['auth_token']);
            this.token = response['auth_token'];
            //console.log("logged")
        },
        async loadUserData(accessToken = ""){
            if(this.token !== "") {
                accessToken = this.token
            }
            if(accessToken != ""){
               // console.log("getting user data")
                const response = (await usersApi.getMyUser(accessToken))['data']
                this.user = response
                await this.loadPersonFriends(response['id'], accessToken)
            }
        },
        async loadPersonFriends(id, accessToken = ""){
            if(this.token !== "") {
                accessToken = this.token
            }
            const response = (await usersApi.getUserFrieds(id, accessToken))['data']
            this.friend = response['friends']
        },
        async loadSideUserData(id){
            const response = (await usersApi.getUser(id, this.token))['data']
            //console.log(response)
            this.sideUser = response
            //console.log(1, this.sideUser)

        },
        async addFriend(data){
            const response = (await  usersApi.addFriend(data, this.token))
        },
        async deleteFriend(data){
            const response = (await  usersApi.deleteFriend(data, this.token))
        },
        async logoutUser() {
            this.user = '';
            this.token = '';
            return "success";
        },
        async updateUser(data) {
            const accessToken = this.token
            const userId = (this.user)['id']
            const response = (await usersApi.userUpdate(accessToken, data, userId))['data'];
            this.user = response;
        },
        async createUser(data) {
            const response = (await usersApi.userRegistration(data))['data'];
            const nData = {}
            nData['password'] = data['password']
            nData['username'] = data['username']
            await this.loginUser(nData);
        },
    },
});

export default usersStore;