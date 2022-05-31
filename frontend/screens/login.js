// Formik x React Native example

import React from "react";

import { Button, TextInput, View } from "react-native";

import { Formik } from "formik";
import { Text } from "react-native-elements";

const Login = (props) => (
  <Formik
    initialValues={{ email: "" }}
    onSubmit={(values) => console.log(values)}
  >
    {({ handleChange, handleBlur, handleSubmit, values }) => (
      <View>
        <Text> Email </Text>
        <TextInput
          onChangeText={handleChange("email")}
          onBlur={handleBlur("email")}
          value={values.email}
        />

        <Button onPress={handleSubmit} title="Submit" />
      </View>
    )}
  </Formik>
);
export default Login;
