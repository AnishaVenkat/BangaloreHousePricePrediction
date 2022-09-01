from flask import Flask,request,render_template

app=Flask(__name__)
import pandas as pd
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
import pickle

pickle_in = open("banglore_home_prices_model.pickle", 'rb')
model = pickle.load(pickle_in)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/bglrpred",methods=['POST'])
def predict():
    if request.method=='POST':

        Size=float(request.form['Size'])
        Total_sqft=float(request.form['Total_sqft'])
        Bath=int(request.form['Bath'])

        data_list=[Size,Total_sqft,Bath]
        data = pd.DataFrame(data_list,index=["Size","Total_sqft","Bath"]).T
        Location=request.form['Location']

        location_list = ["Devarachikkanahalli", "1st block jayanagar", "1st phase jp nagar",
                         "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout",
                         "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar",
                         "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", "ambalipura",
                         "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura",
                         "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout",
                         "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii",
                         "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi",
                         "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar",
                         "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar",
                         "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra",
                         "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar",
                         "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar",
                         "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura",
                         "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur",
                         "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city",
                         "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya",
                         "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout",
                         "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout",
                         "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road",
                         "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli",
                         "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar",
                         "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram",
                         "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli",
                         "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura",
                         "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar",
                         "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town",
                         "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu",
                         "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate",
                         "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura",
                         "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra",
                         "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout",
                         "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi",
                         "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar",
                         "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout",
                         "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout",
                         "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar",
                         "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar",
                         "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road",
                         "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar",
                         "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura",
                         "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya",
                         "thubarahalli", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road",
                         "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout",
                         "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town",
                         "yelenahalli", "yeshwanthpur"]
        loc_val = []

        area_list = ["Built-up Area", "Carpet Area", "Plot Area", "Super built-up Area"]
        area_val = []

        for i in location_list:
            if i == Location:
                val = 1
                loc_val.append(val)
            if i != Location:
                val = 0
                loc_val.append(val)

        loc_df = pd.DataFrame(loc_val, index=location_list).T
        Area=request.form['Area']

        for j in area_list:
            if j == Area:
                value = 1
                area_val.append(value)
            if j != Area:
                value = 0
                area_val.append(value)

        area_df = pd.DataFrame(area_val, index=area_list).T

        df=pd.concat([data,loc_df,area_df],axis=1)

        prediction=model.predict(df)
        print(prediction)
        output = round(prediction[0],2)

        if output < 0:
            return render_template('index.html', prediction_text="Sorry you cannot buy this house")
        else:
            return render_template('index.html', prediction_text="You Can buy The house at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()