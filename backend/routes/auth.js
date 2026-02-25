const router = require("express").Router();
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/User");


// ⭐ GET test route
router.get("/", (req,res)=>{
    res.send("Auth API working 🚀");
});

// ⭐ GET register route (for browser testing only)
router.get("/register", (req,res)=>{
    res.send("Use POST method to register");
});

// ⭐ REGISTER (POST)
router.post("/register", async(req,res)=>{
 const hash = await bcrypt.hash(req.body.password,10);
 await new User({email:req.body.email,password:hash}).save();
 res.send("Registered");
});


// ⭐ GET login route (browser testing)
router.get("/login", (req,res)=>{
    res.send("Use POST method to login");
});

// ⭐ LOGIN (POST)
router.post("/login", async(req,res)=>{
 const user = await User.findOne({email:req.body.email});
 if(!user) return res.send("No user");

 const ok = await bcrypt.compare(req.body.password,user.password);
 if(!ok) return res.send("Wrong password");

 const token = jwt.sign({id:user._id},"secret");
 res.json({token});
});

module.exports = router;