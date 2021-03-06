import {
    StyleSheet
} from "react-native";

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
        justifyContent: "center",
    },

    detailContainer: {
        padding:"10px",
        flex: 1,
        backgroundColor: "#fff",
    },
    

    listPage: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "left",
        justifyContent: "center",
    },

    image: {
        marginBottom: 40,
    },

    inputView: {
        backgroundColor: "#FFC0CB",
        borderRadius: 8,
        width: "80%",
        height: 45,
        marginBottom: 20,
        alignItems: "center",
        justifyContent: "center",

    },

    TextInput: {
        flex: 1,
        width: "97%",
        margin:6,
        padding:10
    },

    forgot_button: {
        height: 30,
        marginBottom: 30,
    },

    loginBtn: {
        width: "80%",
        borderRadius: 25,
        height: 50,
        alignItems: "center",
        justifyContent: "center",
        marginTop: 40,
        backgroundColor: "#FF1493",
    },
    plcBtn:{
        width: "95%",
        borderRadius: 25,
        height: 50,
        marginTop:"auto",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#FF1493",        
    },
    loginText: {
        color:"#EEE",
    },
    listContainer:{
        width: "97%",
        height:"90%"
    },


    listItem: {
        width: "100%",
        height: 120,
        backgroundColor: '#EFEFEF',
        padding: 20,
        marginVertical: 8,
        borderColor: "#EEE",
        borderWidth: 1,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 1,
        },
        shadowOpacity: 0.22,
        shadowRadius: 2.22,

        elevation: 3,
    },
    storeMarker:{
        backgroundColor: '#FFF',
        borderColor: "#DEE",
        borderWidth: 2,
        width:"120px",
        height: '25px',
        alignSelf: 'flex-start',
        borderRadius: 15,
        alignItems: "center",
        flexDirection:'row',
    },
    floating: {
        height: '40px',
        width: '40px',
        position: 'absolute',
        left: 10,
        top: 10,
        backgroundColor: '#FFF',
        borderColor: "#EEE",
        borderWidth: 1,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.23,
        shadowRadius: 2.62,
        alignItems: "center",
        justifyContent: "center",
        elevation: 4,
    }
});

export default styles; 