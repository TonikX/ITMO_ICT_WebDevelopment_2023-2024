class UsersApi {
    constructor(instance) {
        this.API = instance;
    }

    userLogin = async (data) => {
        return this.API({
            method: "POST",
            url: "/auth/token/login",
            data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        });
    };

    getMyUser = async (token) => {
        return this.API({
            method: "GET",
            url: "/auth/users/me",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            }
        });
    };

    getUser = async (id, token) => {
        return this.API({
            method: "GET",
            url: `/person/${id}`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    getUserFrieds = async (id, token) => {
        return this.API({
            method: "GET",
            url: `/person/${id}/friends`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    addFriend = async (data, token) => {
        return this.API({
            method: "POST",
            url: `/person/addfriend`,
            data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    deleteFriend = async (data, token) => {
        return this.API({
            method: "DELETE",
            url: `/person/deletefriend/${data['fromPersonID']}/${data['toPersonID']}`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    userRegistration = async (data) => {
        //console.log("Api", data);
        return this.API({
            method: "POST",
            url: "/auth/users/",
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        });
    };

    userUpdate = async (token, data, userId) => {
        return this.API({
            method: "PATCH",
            url: `/person/update/${userId}`,
            data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };
}

export default UsersApi;