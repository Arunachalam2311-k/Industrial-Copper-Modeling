import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder

# ----------------------------------------------------------------------------------

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color:blue;'>INDUSTRIAL COPPER MODELING</h1>", unsafe_allow_html=True)
selected = option_menu(None, ['Price prediction', 'Status prediction'],
                        orientation='horizontal', default_index=0)

if selected == 'Price prediction':
        
        try:
            item_list = ['W', 'S', 'Others', 'PL', 'WI', 'IPL']
            status_list = ['Won', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
            country_list = ['28', '32', '38', '78', '27', '30', '25', '77', '39', '40', '26', '84', '80', '79', '113', '89']
            application_list = [10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 40, 25, 67, 79, 3, 99, 2, 5, 39, 69, 70, 65, 58, 68]
            product_list = [1670798778, 1668701718, 628377, 640665, 611993, 1668701376, 164141591, 1671863738, 1332077137, 640405,
                            1693867550, 1665572374, 1282007633, 1668701698, 628117, 1690738206, 628112, 640400, 1671876026, 164336407,
                            164337175, 1668701725, 1665572032, 611728, 1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
                            1665584320, 1665584662, 1665584642]

            c1, c2 = st.columns([2, 2])

            with c1:
                    quantity = st.text_input('**Enter Quantity (Min:4.235594 & Max:151.44810389856653) in tons**')
                    thickness = st.text_input('**Enter Thickness (Min:0.18 & Max:6.449999999999999)**')
                    width = st.text_input('**Enter width (Min:700.0 & Max: 1980.0)**')
                    customer = st.text_input("Customer ID (Min:12458.0, Max:2147483647.0)")

    
            with c2:
                    country = st.selectbox('**Country Code**', country_list)
                    status = st.selectbox('**Status**', status_list)
                    item = st.selectbox('**Item Type**', item_list)
                    application = st.selectbox('**Application Type**', application_list)
                    product = st.selectbox('**Product Reference**', product_list)

            with c1:
                    st.write('')
                    st.write('')
                    st.write('')
                    st.write('')
                    if st.button('PREDICT PRICE'):
                        data = []

                    # Load encoded data and scaler
                    with open('country.pkl', 'rb') as file:
                        encode_country = pickle.load(file)
                    with open('status.pkl', 'rb') as file:
                        encode_status = pickle.load(file)
                    with open('item type.pkl', 'rb') as file:
                        encode_item = pickle.load(file)
                    with open('scaling.pkl', 'rb') as file:
                        scaler = pickle.load(file)

            

                    with open('ExtraTreesRegressor.pkl', 'rb') as file:
                        model = pickle.load(file)

                    encode = LabelEncoder()
                    encode_country=encode.fit(country_list)

                    trns_country = encode_country.transform(country_list)
                    encoded_ct = None
                    for i,j in zip(country_list,trns_country):
                        if country ==i:
                            encoded_ct =j
                            break
                    else:
                        st.error("country not found.")
                        exit()

                    encode = LabelEncoder()
                    encode_country=encode.fit(status_list)

                    trns_status= encode_country.transform(status_list)
                    encoded_st = None
                    for i,j in zip(status_list,trns_status):
                        if status ==i:
                            encoded_st =j
                            break
                    else:
                        st.error("status not found.")
                        exit()


                    encode = LabelEncoder()
                    encode_country=encode.fit(item_list)

                    trns_item = encode_country.transform(item_list)
                    encoded_it = None
                    for i, j in zip(item_list,trns_item):
                        if item ==i:
                            encoded_it =j
                            break
                    else:
                        st.error("item_list not found.")
                        exit()


                    data.append(quantity)
                    data.append(thickness)
                    data.append(width)
                    data.append(customer)
                    data.append(encoded_st)
                    data.append(encoded_ct)
                    data.append(encoded_it)
                    data.append(application)
                    data.append(product)
                    
                    x = np.array(data).reshape(1,-1)
                    pred_model = scaler.transform(x)
                    price_predict = model.predict(pred_model)
                    predicted_price = str(price_predict)[1:-1]

                    st.success(f'**Predicted Selling Price : :green[₹] :green[{predicted_price}]**')

    
        except:
            st.error('Please enter values in empty cells')



# status prediction

if selected =='Status prediction':

    try:
        if 'Status prediction':
            item_list1 = ['W', 'WI', 'S', 'Others', 'PL', 'IPL']
            country_list1 = [28., 25., 30., 32., 38., 27., 78., 77., 26., 84., 113., 39., 40., 80., 79., 107.]
            application_list1 = [10., 41., 28., 59.,  4., 38., 42., 15., 56., 26., 20., 66., 29.,22., 25., 40., 27.,  3., 67.,  2.,  5., 79., 39., 69., 19., 65.,
                                58., 70., 68., 99.]
            product_list1 = [1670798778, 1668701718,     628377,     640665,     611993,1668701376,  164141591, 1332077137, 1671863738, 
                            640405,1693867550, 1282007633, 1668701698, 1665572374,
                            628112,164336407, 1690738206,     611728, 1721130331,   640400,
                            1693867563, 1671876026,     628117,     611733, 1722207579,
                            164337175,  929423819, 1668701725, 1665584642]
            
            s1,s2 = st.columns([2,2])
            with s1:
                quantity1 = st.text_input('ENTER QUANTITY (Min:4.235594 & Max:151.44810389856653) in tons')
                thickness1 = st.text_input("ENTER THICKNESS (Min:0.18 & Max:6.449999999999999)")
                width1 = st.text_input('ENTER WIDTH (Min:700.0 & Max: 1980.0)')
                customer1 = st.text_input("Customer ID (Min:12458.0, Max:2147483647.0)")
                selling1 = st.text_input("Selling Price (Min:243.0, Max:1379.0)")

            with s2:
                country1 = st.selectbox('**Country Code**', country_list1)
                item1 = st.selectbox('**Item Type**', item_list1)
                application1 = st.selectbox('**Application Type**', application_list1)
                product1 = st.selectbox('**Product Reference**', product_list1)

            with s1:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                if st.button('PREDICT STATUS'):
             
                    quantity1 = float(quantity1) if quantity1 else None
                    thickness1 = float(thickness1) if thickness1 else None
                    width1 = float(width1) if width1 else None
                    customer1 = float(customer1) if customer1 else None
                    selling1 = float(selling1) if selling1 else None
                    data_cls=[]
                                   
                    with open('country.pkl','rb')as file:
                        encode_country_cls = pickle.load(file)
                    with open('item type.pkl','rb')as file:
                        encode_item_cls = pickle.load(file)
                    with open('scaling_classify.pkl',"rb") as file:
                        scaler=pickle.load(file)
                    with open('RandomForestClassifier.pkl','rb')as file:
                        trained_model_cls = pickle.load(file)

                    encode=LabelEncoder()
                    encode_country_cls = encode.fit(country_list1 )

                    trns_country_cls = encode_country_cls.transform(country_list1)
                    encoded_ct_cls = None
                    for i,j in zip(country_list1,trns_country_cls):
                        if country1 ==i:
                            encoded_ct_cls=j
                            break
                    else:
                        st.error('country not found..')


                    encode=LabelEncoder()
                    encode_item_cls = encode.fit(item_list1)

                    trns_item_cls = encode_item_cls.transform(item_list1)
                    encoded_it_cls = None
                    for i,j in zip(item_list1,trns_item_cls):
                        if item1 ==i:
                            encoded_it_cls=j
                            break
                    else:
                        st.error('item type not found..')


                    data_cls.append(quantity1)
                    data_cls.append(thickness1)
                    data_cls.append(width1)
                    data_cls.append(customer1)
                    data_cls.append(selling1)
                    data_cls.append(encoded_it_cls)
                    data_cls.append(encoded_ct_cls)
                    data_cls.append(application1)
                    data_cls.append(product1)

                    x_cls = np.array(data_cls).reshape(1, -1)
                    scaler_cls = scaler.transform(x_cls)
                    pred_status = trained_model_cls.predict(scaler_cls)

                    if pred_status == 1:
                        st.success('**Predicted Status: :green[WON]**')
                    else:
                        st.error('**Predicted Status: :red[LOST]**')
    except:
        st.error("Please enter values in empty cells") 