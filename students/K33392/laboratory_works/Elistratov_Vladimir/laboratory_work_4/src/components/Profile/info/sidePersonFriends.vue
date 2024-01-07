<script>
  import usersStore from "@/stores/user.js";
  import capsulesStore from "@/stores/capsules.js";

  export default {
    name: 'sidePersonFriends',
    data(){
      return{
        usState: usersStore(),
      }
    },
    props: {
      flag: {
        type: Boolean,
      },
      targetUserId: {
        type: Number,
      },
      fromUserId: {
        type: Number,
      }
    },
    methods: {
      changeFriendship(flag){
        if(flag){
          let data = {}
          data['fromPersonID'] = this.fromUserId
          data['toPersonID'] = this.targetUserId
          this.usState.addFriend(data)
          this.usState.loadPersonFriends(this.fromUserId)
          this.friends = this.usState.friend
          location.href=`/vaulttec/profile/${this.fromUserId}`
        }
        else{
          let data = {}
          data['fromPersonID'] = this.fromUserId
          data['toPersonID'] = this.targetUserId
          this.usState.deleteFriend(data)
          this.usState.loadPersonFriends(this.fromUserId)
          this.friends = this.usState.friend
          location.href=`/vaulttec/profile/${this.fromUserId}`
        }
      }
    },
  }
</script>

<template>
  <div class="justify-s-b">
    <div v-if="this.flag">
      <button type="button" class="btn btn-lg btn-my-main" @click="changeFriendship(true)">
        Добавить в друзья
      </button>
    </div>
    <div v-else>
      <button type="button" class="btn btn-lg btn-my-main" @click="changeFriendship(false)">
        Удалить из друзей
      </button>
    </div>
  </div>
</template>

<style scoped>

</style>