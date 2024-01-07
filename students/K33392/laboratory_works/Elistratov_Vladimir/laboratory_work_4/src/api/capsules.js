class CapsulesApi {
    constructor(instance) {
        this.API = instance;
    }

    getOneCapsule = async(id, userId, token) => {
        return await this.API({
            method: "GET",
            url: `/vault/${id}/${userId}`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    }

    getAllCapsules = async () => {
        return this.API({
            method: "GET",
            url: "/vault/all",
        });
    };

    getMyCapsules = async (userId, token) => {
        return this.API({
            method: "GET",
            url: `/vault/my/${userId}`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };
    getNotMyCapsules = async (userId, token) => {
        return this.API({
            method: "GET",
            url: `/vault/notmy/${userId}`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    getOpenedCapsules = async () => {
        return this.API({
            method: "GET",
            url: `/vault/opened`,
        });
    };

    getClosedCapsules = async () => {
        return this.API({
            method: "GET",
            url: `/vault/closed`,
        });
    };

    createCapsule = async (data, token) => {
        return this.API({
            method: "POST",
            url: "/vault/create",
            data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

}

export default CapsulesApi;