<template xmlns="http://www.w3.org/1999/html">
  <header class="rounded">
    <profile-header/>
  </header>
  <main class="rounded">
    <div v-if="this.state">
      <profile-info
          :userName="this.userD['username']"
          :firstName="this.userD['first_name']"
          :lastName="this.userD['last_name']"
          :email="this.userD['email']"
          :dateJoined="this.userD['date_joined']"
          :capCount="this.userD['capCount']"
      />
    </div>
    <div v-else>
      <side-profile-info
          :userName="this.sideUserD['username']"
          :firstName="this.sideUserD['first_name']"
          :lastName="this.sideUserD['last_name']"
          :capCount="this.sideUserD['capCount']"
      />
    </div>

  </main>

  <main>
    <h2>Друзья</h2>
    <hr class="content-dividing-line rounded mt-3 mb-3"/>
    <div v-if="this.state" id="friendsList" class="row">
      <div class="col-xl-3 col-md-4 col-sm-6 mb-3" v-for="friend in friends" :key="friend.id">
        <friends-list
            :id=friend.id
            :userName="friend.username"
            :firstName="friend.first_name"
            :lastName="friend.last_name"
        />
      </div>
    </div>
    <div v-else>
      <side-person-friends
        :flag=friendsCheck()
        :targetUserId="this.sideUserD['id']"
        :fromUserId="this.userD['id']"
      />
    </div>
  </main>
  <footer>
    <footer-c/>
  </footer>
  <profile-update-modal/>
</template>

<style scoped>

</style>

<script>
  import usersStore from "@/stores/user.js";
  import capsulesStore from "@/stores/capsules.js";
  import ProfileHeader from "@/components/Profile/Header/ProfileHeader.vue";
  import FooterC from "@/components/footerC.vue";
  import ProfileInfo from "@/components/Profile/info/profileInfo.vue";
  import VaultOpened from "@/components/Main/Vaults/vaultOpened.vue";
  import SideProfileInfo from "@/components/Profile/info/sideProfileInfo.vue";
  import router from "@/router/index.js";
  import {useUserLoad} from "@/composables/userLoad.js";
  import FriendsList from "@/components/Profile/info/friendsList.vue";
  import SidePersonFriends from "@/components/Profile/info/sidePersonFriends.vue";
  import ProfileUpdateModal from "@/components/Profile/updateModal.vue";

  export default {
    name: "profilePage",
    data(){
      return{
        usState: usersStore(),
        capState: capsulesStore(),
        userD: {},
        sideUserD: {},
        friends: {},
        state: false,
      }
    },
    props: {
      userId: {
        type: String,
      },
    },
    components: {
      ProfileUpdateModal,
      SidePersonFriends,
      FriendsList,
      SideProfileInfo,
      VaultOpened,
      ProfileInfo,
      FooterC,
      ProfileHeader
    },
    methods: {
      friendsCheck(){
        let flag = true;
        //console.log(this.userId, this.userD)
        for (let friend in this.friends){
          //console.log(this.userD['id'], this.friends[friend]['id'])
          if(this.sideUserD['id'] == this.friends[friend]['id']){
            flag = false;
            break;
          }
        }
        return flag
      },

    },
    async mounted() {
      await this.usState.loadUserData()
      this.friends = this.usState.friend
      this.userD = this.usState.user
      const flag = await useUserLoad(this.userId, this.userD['id'])
      if(flag){
        this.state = true
      }
      else{
        this.sideUserD = this.usState.sideUser
      }
    }
  };

</script>