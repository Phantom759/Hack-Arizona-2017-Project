package hackzilla.familiarfaces;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.Reader;
import java.util.Scanner;


public class PhotoGrabber extends Activity {
    ImageButton click;
    ImageView result;
    static final int REQUEST_IMAGE_CAPTURE = 1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_photo_grabber);

        click = (ImageButton) findViewById(R.id.camera);
        result = (ImageView) findViewById(R.id.image_view);

    }

    public void dispatchTakePictureIntent(View view) {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");
            result.setImageBitmap(imageBitmap);
            File image = new File("temp");
            Uri uriImageData = Uri.fromFile(image);
            data.putExtra(MediaStore.EXTRA_OUTPUT, uriImageData);


            File pythonToJavaFile = new File("storage/emulated/0/DCIM/Camera/PythontoJava.txt");
            boolean fileExists = pythonToJavaFile.exists();

            while(!fileExists) {
                fileExists = pythonToJavaFile.exists();
            }
                Scanner scanner = null;
            try {
                scanner = new Scanner(pythonToJavaFile);
                System.out.println("FOUND THE P2J FILE");
            }
            catch(IOException e){
                System.out.println("NO P2J FILE!");
                e.printStackTrace();
            }
            String text = "";
            while (scanner.hasNextLine()) {
                text += scanner.nextLine();
                System.out.println("GOT A LINE!");
            }
            System.out.println("RESULT IS "+text);
            scanner.close();
            pythonToJavaFile.delete();



            // CALL JYTHON CODE
            /*   Method returns a comma-separated String
                 Requires package org.jython.book.interfaces;
                 public interface
            */
            /*String[] cmd = {
                    "~",
                    "mkdir pleaseDearLordWorkNowPLeasePlease"
            };
            try {
                Runtime.getRuntime().exec(cmd);
                System.out.print("Run");
            }catch (Exception e){
                System.err.print("cry");
            }*/
            //System.out.println("SAVED IMAGE");

        }
    }

}
