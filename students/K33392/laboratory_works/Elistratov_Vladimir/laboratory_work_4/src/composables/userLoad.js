import usersStore from "@/stores/user.js";
import router from "@/router/index.js";

export async function useUserLoad(userId, currentUserId){
    let usState = usersStore()
    if(usState.token != ""){
        if(userId != currentUserId){
            await usState.loadSideUserData(userId)
            return false
        }
        else{
            return true
        }
    }
    else{
        router.push({name: 'main'})
    }
}