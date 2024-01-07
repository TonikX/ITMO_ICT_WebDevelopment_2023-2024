import instance from "@/api/instance";
import CapsulesApi from "@/api/capsules.js";
import UsersApi from "@/api/user.js";
import CommentsApi from "@/api/comments.js";

const capsulesApi = new CapsulesApi(instance);
const usersApi = new UsersApi(instance);
const commentsApi = new CommentsApi(instance)


export {
    capsulesApi,
    usersApi,
    commentsApi,
}