class CommentsApi {
    constructor(instance) {
        this.API = instance;
    }

    getVaultComments = async (vaultId, token) => {
        return this.API({
            method: "GET",
            url: `/vault/comments/${vaultId}/`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };

    createComments = async (data, token) => {
        return this.API({
            method: "POST",
            url: `/vault/comments/create`,
            data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
            }
        });
    };


}

export default CommentsApi;