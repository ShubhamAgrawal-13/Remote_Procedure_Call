// Import required java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

// import java.io.IOException;
// import java.io.PrintWriter;
import java.util.Enumeration;
 
// import javax.servlet.http.HttpServlet;
// import javax.servlet.http.HttpServletRequest;
// import javax.servlet.http.HttpServletResponse;

// Extend HttpServlet class
public class ServerRPC extends HttpServlet {
 
   private String message;
   private String[] methods={"sum 2","multiply 2","max3 3","sqrt 1"};

   public void init() throws ServletException {
      // Do required initialization
      message = "Hello World";
   }

   public int sum(int a,int b)
   {
      return a+b;
   }

   public int multiply(int a,int b)
   {
      return a*b;
   }

   public int max3(int a,int b,int c)
   {
      return Math.max(Math.max(a,b),c);
   }

   public double sqrt(int a)
   {
      return Math.sqrt(a);
   }

   public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        handleRequest(request, response);
    }
 
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        handleRequest(request, response);
    }

    public void handleRequest(HttpServletRequest request, HttpServletResponse response) throws IOException {
 
        PrintWriter out = response.getWriter();
        response.setContentType("text/html");

        Enumeration<String> parameterNames = request.getParameterNames();
        String paramName = parameterNames.nextElement();
        if(paramName.equals("method"))
        {
            for(String method : methods)
            {
                out.write(method+":");
            }
        }
        else if(paramName.equals("sum"))
        {
            String[] paramValues = request.getParameterValues(paramName);
            int a=0,b=0;
            a=Integer.valueOf(paramValues[0]);
            b=Integer.valueOf(paramValues[1]);
            out.write(String.valueOf(sum(a,b)));
        }
        else if(paramName.equals("multiply"))
        {
            String[] paramValues = request.getParameterValues(paramName);
            int a=0,b=0;
            a=Integer.valueOf(paramValues[0]);
            b=Integer.valueOf(paramValues[1]);
            out.write(String.valueOf(multiply(a,b)));
        }
        else if(paramName.equals("max3"))
        {
            String[] paramValues = request.getParameterValues(paramName);
            int a=0,b=0,c=0;
            a=Integer.valueOf(paramValues[0]);
            b=Integer.valueOf(paramValues[1]);
            c=Integer.valueOf(paramValues[2]);
            out.write(String.valueOf(max3(a,b,c)));
        }
        else if(paramName.equals("sqrt"))
        {
            String[] paramValues = request.getParameterValues(paramName);
            int a=0;
            a=Integer.valueOf(paramValues[0]);
            out.write(String.valueOf(sqrt(a)));
        }

        // int sum=0;
        // while (parameterNames.hasMoreElements()) {
        //     String paramName = parameterNames.nextElement();
        //     // out.write(paramName);
        //     // out.write(" ");
        //     String[] paramValues = request.getParameterValues(paramName);
        //     for (int i = 0; i < paramValues.length; i++) 
        //     {
        //         String paramValue = paramValues[i];
        //         out.write(":" + paramValue);
        //         out.write(" ");
        //     }
        // }

        //out.println("<h1>" + message + "</h1>");
   }

   public void destroy() {
      System.out.println("destroyed");
      // do nothing.
   }
}